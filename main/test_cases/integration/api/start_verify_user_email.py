from django.core import mail
from django.core.cache import cache
from django.utils.http import urlencode
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class StartVerifyUserEmailApiTestCase(ApiTestCase):
    fixtures = ["user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.post(reverse("api-user-start-verify-email"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.post(reverse("api-user-start-verify-email"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        sentinel = object()
        token = cache.get("verify_user_email.1", sentinel)
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            f"http://testserver/user/verify_email?{urlencode({'token': token})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email1@email.com", mail.outbox[0].to)
