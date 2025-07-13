from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class DeleteUserApiTestCase(ApiTestCase):
    fixtures = ["users"]

    def test(self) -> None:
        """Test success case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.delete(reverse("api-user"))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=1).exists())
