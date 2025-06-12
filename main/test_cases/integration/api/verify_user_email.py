from secrets import token_urlsafe

from django.core.cache import cache
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class VerifyUserEmailApiTestCase(ApiTestCase):
    fixtures = ["user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.post(reverse("api-user-verify-email"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 600)
        response = self.client.post(
            reverse("api-user-verify-email"), data={"token": token}
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        user.refresh_from_db()
        self.assertTrue(user.email_is_verified)

    def test_incorrect_token(self) -> None:
        """Test incorrect token case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 600)
        response = self.client.post(
            reverse("api-user-verify-email"), data={"token": f"{token}_"}
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"token": ["incorrect token"]})

    def test_token_not_found(self) -> None:
        """Test token not found case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        response = self.client.post(
            reverse("api-user-verify-email"), data={"token": token_urlsafe()}
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"token": ["token not found"]})
