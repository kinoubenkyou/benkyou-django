from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from main.models import User
from main.tests.integration.api import ApiTestCase


class DeleteUserApiTestCase(ApiTestCase):
    fixtures = ["user"]  # type: ignore[assignment]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.delete(reverse("api-user"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.delete(reverse("api-user"))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=1).exists())
