from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from main.models import User
from main.tests.integration.api import ApiTestCase


class UpdateUserApiTestCase(ApiTestCase):
    fixtures = ["user"]  # type: ignore[assignment]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.put(reverse("api-user"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        username = "username01"
        last_name = "last_name01"
        first_name = "first_name01"
        email = "email01@email.com"
        response = self.client.put(
            reverse("api-user"),
            data={
                "username": username,
                "last_name": last_name,
                "first_name": first_name,
                "email": email,
            },
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.username, username)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.email, email)
