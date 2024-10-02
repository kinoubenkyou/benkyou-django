from datetime import UTC, datetime

from selenium.webdriver.common.by import By

from main.documents import OrganizationActivity
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

    def test_success(self):
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

        self.web_driver.find_element(By.XPATH, '//input[@name="per_page"]').send_keys(
            "2",
        )
        self.web_driver.find_element(
            By.XPATH,
            '//select[@name="sort_by"]//option[@value="timestamp"]',
        ).click()
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        for index in range(1, 3):
            self.assertEqual(self.count_row(index), 1)

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

        for index in range(11, 12):
            self.assertEqual(self.count_row(index), 1)

        self.web_driver.find_element(
            By.XPATH,
            '//a[normalize-space(text())="Previous"]',
        ).click()

        for index in range(9, 11):
            self.assertEqual(self.count_row(index), 1)

        self.web_driver.find_element(
            By.XPATH,
            '//a[normalize-space(text())="First"]',
        ).click()

        for index in range(1, 3):
            self.assertEqual(self.count_row(index), 1)
