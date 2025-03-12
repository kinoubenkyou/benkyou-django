from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from main.models import User
from main.tests.integration.api import ApiTestCase


class ReadUserApiTestCase(ApiTestCase):
    fixtures = ["user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("api-user"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(reverse("api-user"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        actual_data = response.json()
        self.assertEqual(actual_data["last_login"], "2000-01-01T00:00:00Z")
        self.assertEqual(actual_data["username"], "username1")
        self.assertEqual(actual_data["first_name"], "first_name1")
        self.assertEqual(actual_data["last_name"], "last_name1")
        self.assertEqual(actual_data["email"], "email1@email.com")
        self.assertEqual(actual_data["date_joined"], "2000-01-01T00:00:00Z")
