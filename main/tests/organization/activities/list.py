from datetime import UTC, datetime

from django.test import override_settings
from selenium.webdriver.common.by import By

from main.documents import OrganizationActivity
from main.models import User
from main.tests.mixin import SwitchOrganizationMixin
from main.tests.shortcuts import format_datetime
from main.tests.test_case import TestCase


class OrganizationActivitiesListTestCase(SwitchOrganizationMixin, TestCase):
    def count_row(self, index):
        return len(
            self.find_rows_with_texts(
                f"action{index}",
                format_datetime(datetime(1, 1, index, tzinfo=UTC)),
                "email1@email.com",
                f"code{index}",
                f"name{index}",
            ),
        )

    @override_settings(DEBUG=True)
    def test(self):
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action=f"action{index}",
                    data={"code": f"code{index}", "name": f"name{index}"},
                    object_id=1,
                    timestamp=datetime(1, 1, index, tzinfo=UTC),
                    user_id=1,
                )
                for index in range(1, 12)
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities")
        self.sign_in()
        self.switch_organization()

        self.assertEqual(
            len(self.web_driver.find_elements(By.XPATH, "//tbody//tr")),
            10,
        )
        for index in range(2, 12):
            self.assertEqual(self.count_row(index), 1)

    def test_paginate(self):
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action=f"action{index}",
                    data={"code": f"code{index}", "name": f"name{index}"},
                    object_id=1,
                    timestamp=datetime(1, 1, index, tzinfo=UTC),
                    user_id=1,
                )
                for index in range(1, 6)
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities")
        self.sign_in()
        self.switch_organization()
        self.web_driver.find_element(By.XPATH, '//input[@name="per_page"]').send_keys(
            "2",
        )
        self.web_driver.find_element(
            By.XPATH,
            '//select[@name="sort_by"]//option[@value="timestamp"]',
        ).click()
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver.find_element(
            By.XPATH,
            '//a[normalize-space(text())="Next"]',
        ).click()

        for index in range(3, 5):
            self.assertEqual(self.count_row(index), 1)

        self.web_driver.find_element(
            By.XPATH,
            '//a[normalize-space(text())="Last"]',
        ).click()

        for index in range(5, 6):
            self.assertEqual(self.count_row(index), 1)

        self.web_driver.find_element(
            By.XPATH,
            '//a[normalize-space(text())="Previous"]',
        ).click()

        for index in range(3, 5):
            self.assertEqual(self.count_row(index), 1)

        self.web_driver.find_element(
            By.XPATH,
            '//a[normalize-space(text())="First"]',
        ).click()

        for index in range(1, 3):
            self.assertEqual(self.count_row(index), 1)

    def test_filter__timestamp(self):
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action=f"action{index}",
                    data={"code": f"code{index}", "name": f"name{index}"},
                    object_id=1,
                    timestamp=datetime(1, 1, index, tzinfo=UTC),
                    user_id=1,
                )
                for index in range(1, 5)
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities")
        self.sign_in()
        self.switch_organization()
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="timestamp__gte"]',
        ).send_keys("01020001")
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="timestamp__lt"]',
        ).send_keys("01030001")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        for index in range(2, 4):
            self.assertEqual(self.count_row(index), 1)

    def test_filter__user_id(self):
        User.objects.bulk_create(
            [
                User(
                    email=f"email{index}@email.com",
                    email_verified=True,
                    name=f"name{index}",
                )
                for index in range(2, 3)
            ],
        )
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action=f"action{index}",
                    data={"code": f"code{index}", "name": f"name{index}"},
                    object_id=1,
                    timestamp=datetime(1, 1, index, tzinfo=UTC),
                    user_id=index,
                )
                for index in range(1, 3)
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities")
        self.sign_in()
        self.switch_organization()
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="user_id"]',
        ).send_keys("email1@email.com")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        for index in range(1, 2):
            self.assertEqual(self.count_row(index), 1)

    def test_filter__action(self):
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action="action",
                    data={"code": "code", "name": "name"},
                    object_id=1,
                    timestamp=datetime(1, 1, 1, tzinfo=UTC),
                    user_id=1,
                ),
                OrganizationActivity(
                    action="update",
                    data={"code": "code", "name": "name"},
                    object_id=1,
                    timestamp=datetime(1, 1, 1, tzinfo=UTC),
                    user_id=1,
                ),
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities")
        self.sign_in()
        self.switch_organization()
        self.web_driver.find_element(
            By.XPATH,
            '//select[@name="action"]//option[@value="update"]',
        ).click()
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(
            len(
                self.find_rows_with_texts(
                    "update",
                    format_datetime(datetime(1, 1, 1, tzinfo=UTC)),
                    "email1@email.com",
                    "code",
                    "name",
                ),
            ),
            1,
        )
