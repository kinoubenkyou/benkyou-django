from main.documents import OrganizationActivity
from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationActivitiesListTestCase(SwitchOrganizationMixin, TestCase):
    def test_success(self):
        OrganizationActivity.objects.insert(
            [
                OrganizationActivity(
                    action="update",
                    data={"code": f"code{index_}", "name": f"name{index_}"},
                    object_id=1,
                    user_id=1,
                )
                for index_ in range(1, 22)
            ],
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities?page=2")
        self.sign_in()
        self.switch_organization()

        for index_ in range(11, 21):
            self.assertEqual(
                len(
                    self.find_rows_with_texts(
                        "update",
                        "email1@email.com",
                        f"code{index_}",
                        f"name{index_}",
                    ),
                ),
                1,
            )
