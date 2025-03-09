from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED

from main.models import User
from main.tests.integration.api import ApiTestCase


class CreateUserApiTestCase(ApiTestCase):
    def test(self) -> None:
        """Test success case."""
        username = "username"
        password = "Dr0wss@p"
        response = self.client.post(
            reverse("api-user"), data={"username": username, "password": password}
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        user = User.objects.filter(username=username).first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(password))
