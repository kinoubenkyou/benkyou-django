from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class UpdateUserApiTestCase(ApiTestCase):
    fixtures = ["users"]

    def test(self) -> None:
        """Test success case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        username = "username1_"
        email = "email01@email.com"
        response = self.client.put(
            reverse("api-user"),
            data={
                "username": username,
                "email": email,
            },
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
