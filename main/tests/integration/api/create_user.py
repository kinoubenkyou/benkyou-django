from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED

from main.models import User
from main.tests.integration.api import ApiTestCase


class CreateUserApiTestCase(ApiTestCase):
    def test(self) -> None:
        """Test success case."""
        username = "username1"
        last_name = "last_name1"
        first_name = "first_name1"
        email = "email1@email.com"
        password = "Dr0wss@p1"
        response = self.client.post(
            reverse("api-user"),
            data={
                "username": username,
                "last_name": last_name,
                "first_name": first_name,
                "email": email,
                "password": password,
            },
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        user = User.objects.filter(username=username).first()
        self.assertIsNotNone(user)
        self.assertEqual(user.last_name, last_name)  # type: ignore[union-attr]
        self.assertEqual(user.first_name, first_name)  # type: ignore[union-attr]
        self.assertEqual(user.email, email)  # type: ignore[union-attr]
        self.assertTrue(user.check_password(password))  # type: ignore[union-attr]
