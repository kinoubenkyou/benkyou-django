from datetime import timedelta

from main.documents import OrganizationActivity
from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationActivitiesListTestCase(SwitchOrganizationMixin, TestCase):
    def test_success(self):
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action=f"action{index}",
                    data={"code": f"code{index}", "name": f"name{index}"},
                    object_id=1,
                    timestamp=self.now + timedelta(days=index),
                    user_id=1,
                )
                for index in range(1, 3)
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities")
        self.sign_in()
        self.switch_organization()

        for index in range(1, 3):
            self.assertEqual(
                len(
                    self.find_rows_with_texts(
                        f"action{index}",
                        "email1@email.com",
                        (self.now + timedelta(days=index)).strftime(
                            "%Y-%m-%d %H:%M:%S",
                        ),
                        f"code{index}",
                        f"name{index}",
                    ),
                ),
                1,
            )
