from main.documents import OrganizationActivity
from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationActivitiesListTestCase(SwitchOrganizationMixin, TestCase):
    def test_success(self):
        OrganizationActivity.objects.create(
            action="update",
            data={"code": "code1", "name": "name1"},
            object_id=1,
            user_id=1,
        )
        OrganizationActivity.objects.create(
            action="update",
            data={"code": "code2", "name": "name2"},
            object_id=1,
            user_id=1,
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities/")
        self.sign_in()
        self.switch_organization()

        self.assertEqual(
            len(
                self.find_rows_with_texts(
                    "update",
                    "email1@email.com",
                    "code1",
                    "name1",
                ),
            ),
            1,
        )
        self.assertEqual(
            len(
                self.find_rows_with_texts(
                    "update",
                    "email1@email.com",
                    "code2",
                    "name2",
                ),
            ),
            1,
        )
