from main.documents import OrganizationActivity
from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationActivitiesListTestCase(SwitchOrganizationMixin, TestCase):
    def test_success(self):
        OrganizationActivity.objects.create(
            action="update",
            data={"code": "-code", "name": "-name"},
            object_id=1,
            user_id=1,
        )
        OrganizationActivity.objects.create(
            action="update",
            data={"code": "code", "name": "name"},
            object_id=1,
            user_id=1,
        )

        self.web_driver.get(f"{self.live_server_url}/organization/activities/")
        self.sign_in()
        self.switch_organization()

        self.assertEqual(
            len(
                self.find_elements_with_texts(
                    "update",
                    "email@email.com",
                    "-code",
                    "-name",
                ),
            ),
            1,
        )
        self.assertEqual(
            len(
                self.find_elements_with_texts(
                    "update",
                    "email@email.com",
                    "code",
                    "name",
                ),
            ),
            1,
        )
