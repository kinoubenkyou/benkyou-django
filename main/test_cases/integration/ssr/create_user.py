from django.core import mail
from django.core.cache import cache
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class CreateUserSsrTestCase(SsrTestCase):
    def test_get(self) -> None:
        """Test get form."""
        response = self.client.get(reverse("user-create"))
        xpath = """
        //form
        [@method='post']
        [//input[@name='username']]
        [//input[@name='last_name']]
        [//input[@name='first_name']]
        [//input[@name='email']]
        [//input[@name='password']]
        [//input[@name='password_confirmation']]
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        username = "username1"
        last_name = "last_name1"
        first_name = "first_name1"
        email = "email1@email.com"
        password = "Dr0wss@p1"
        response = self.client.post(
            reverse("user-create"),
            {
                "username": username,
                "last_name": last_name,
                "first_name": first_name,
                "email": email,
                "password": password,
                "password_confirmation": password,
            },
        )
        self.assertRedirects(response, reverse("user-sign-in"))
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
        self.assertIn(email, mail.outbox[0].to)

    def test_password_and_confirmation_not_match(self) -> None:
        """Test password and confirmation not match case."""
        password = "Dr0wss@p1"
        response = self.client.post(
            reverse("user-create"),
            {
                "username": "username1",
                "last_name": "last_name1",
                "first_name": "first_name1",
                "email": "email1@email.com",
                "password": password,
                "password_confirmation": f"{password}_",
            },
        )
        self.assertEqual(
            len(
                fromstring(response.content).xpath(  # type: ignore[no-untyped-call]
                    "//*[text()='password and confirmation not match']"
                )
            ),
            1,
        )
