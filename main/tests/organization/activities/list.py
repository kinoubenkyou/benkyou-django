from datetime import UTC, datetime

from main.documents import OrganizationActivity
from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


def format_datetime(datetime_):
    return (
        f"{datetime_.day}"
        f" {datetime_.strftime("%b")}"
        f" {datetime_.year:04}"
        f" {datetime_.strftime("%I:%M:%S %p %z")}"
    )


class OrganizationActivitiesListTestCase(SwitchOrganizationMixin, TestCase):
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
                        format_datetime(datetime(1, 1, index, tzinfo=UTC)),
                        "email1@email.com",
                        f"code{index}",
                        f"name{index}",
                    ),
                ),
                1,
            )
