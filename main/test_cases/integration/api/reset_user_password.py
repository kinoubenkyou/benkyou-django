from secrets import token_urlsafe

from django.core.cache import cache
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class ResetUserPasswordApiTestCase(ApiTestCase):
    fixtures = ["users"]

    def test(self) -> None:
        """Test success case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        password = "Dr0wss@p1_"
        response = self.client.post(
            reverse("api-user-reset-password"),
            data={"password": password, "token": token, "username": "username1"},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertTrue(User.objects.get(pk=1).check_password(password))

    def test_incorrect_token(self) -> None:
        """Test incorrect token case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        response = self.client.post(
            reverse("api-user-reset-password"),
            data={
                "password": "Dr0wss@p1_",
                "token": f"{token}_",
                "username": "username1",
            },
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"non_field_errors": ["incorrect token"]})

    def test_token_not_found(self) -> None:
        """Test token not found case."""
        response = self.client.post(
            reverse("api-user-reset-password"),
            data={
                "password": "Dr0wss@p1_",
                "token": token_urlsafe(),
                "username": "username1",
            },
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"non_field_errors": ["token not found"]})

    def test_username_not_found(self) -> None:
        """Test username not found case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        password = "Dr0wss@p1_"
        response = self.client.post(
            reverse("api-user-reset-password"),
            data={"password": password, "token": token, "username": "username1_"},
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"username": ["username not found"]})
