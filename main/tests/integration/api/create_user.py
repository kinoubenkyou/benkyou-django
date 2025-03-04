from django.urls.base import reverse
from rest_framework.test import APILiveServerTestCase

from main.models import User


class CreateUserApiTestCase(APILiveServerTestCase):
    def test(self) -> None:
        """Test success case."""
        username = "username1"
        password = "Dr0wss@p1"
        self.client.post(
            reverse("api-user-list"), data={"username": username, "password": password}
        )
        user = User.objects.first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
