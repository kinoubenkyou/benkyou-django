from django.core import mail
from django.core.cache import cache
from django.utils.http import urlencode
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED

from main.models import User
from main.test_cases.integration.api import ApiTestCase


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
        self.assertFalse(user.email_is_verified)  # type: ignore[union-attr]
        sentinel = object()
        token = cache.get(f"verify_user_email.{user.pk}", sentinel)  # type: ignore[union-attr]
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            f"http://testserver{reverse('user-verify-email')}"
            f"?{urlencode({'token': token})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email1@email.com", mail.outbox[0].to)
