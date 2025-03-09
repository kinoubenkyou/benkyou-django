from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase

from main.models import User


class CreateUserApiTestCase(APILiveServerTestCase):
    def test(self) -> None:
        """Test success case."""
        username = "username"
        password = "Dr0wss@p"
        self.client.post(
            reverse("api-user-list"), data={"username": username, "password": password}
        )
        user = User.objects.filter(username=username).first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(password))
