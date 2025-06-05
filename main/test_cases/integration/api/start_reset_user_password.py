from django.core import mail
from django.core.cache import cache
from django.utils.http import urlencode
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from main.test_cases.integration.api import ApiTestCase


class StartResetUserPasswordApiTestCase(ApiTestCase):
    fixtures = ["user"]

    def test(self) -> None:
        """Test success case."""
        response = self.client.post(
            reverse("api-user-start-reset-password"), {"username": "username1"}
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        sentinel = object()
        token = cache.get("reset_user_password.username1", sentinel)
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            "http://testserver/user/reset_password?"
            f"{urlencode({'token': token, 'username': 'username1'})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Reset Password")
        self.assertIn("email1@email.com", mail.outbox[0].to)

    def test_username_not_found(self) -> None:
        """Test username not found case."""
        response = self.client.post(
            reverse("api-user-start-reset-password"), data={"username": "username1_"}
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"username": ["username not found"]})
