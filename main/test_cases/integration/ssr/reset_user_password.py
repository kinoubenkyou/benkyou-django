from secrets import token_urlsafe

from django.core.cache import cache
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class ResetUserPasswordSsrTestCase(SsrTestCase):
    fixtures = ["user"]

    def test_get(self) -> None:
        """Test get form."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        response = self.client.get(
            f"{reverse('user-reset-password')}"
            f"?{urlencode({'token': token, 'username': 'username1'})}"
        )
        xpath = f"""
        //form
        [@method='post']
        [//input[@name="username" and @value="username1"]]
        [//input[@name="token" and @value="{token}"]]
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        password = "Dr0wss@p1_"
        response = self.client.post(
            f"{reverse('user-reset-password')}"
            f"?{urlencode({'token': token, 'username': 'username1'})}",
            {
                "password": password,
                "password_confirmation": password,
                "token": token,
                "username": "username1",
            },
        )
        self.assertRedirects(response, reverse("user-sign-in"))
        self.assertTrue(User.objects.get(pk=1).check_password(password))

    def test_incorrect_token(self) -> None:
        """Test incorrect token case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        password = "Dr0wss@p1_"
        response = self.client.post(
            f"{reverse('user-reset-password')}"
            f"?{urlencode({'token': f'{token}_', 'username': 'username1'})}",
            {
                "password": password,
                "password_confirmation": password,
                "token": f"{token}_",
                "username": "username1",
            },
        )
        self.assertEqual(
            len(fromstring(response.content).xpath("//*[text()='incorrect token']")),  # type: ignore[no-untyped-call]
            1,
        )

    def test_password_and_confirmation_not_match(self) -> None:
        """Test incorrect password and confirmation not match case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        password = "Dr0wss@p1_"
        response = self.client.post(
            f"{reverse('user-reset-password')}"
            f"?{urlencode({'token': token, 'username': 'username1'})}",
            {
                "password": password,
                "password_confirmation": f"{password}_",
                "token": token,
                "username": "username1",
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

    def test_token_not_found(self) -> None:
        """Test token not found case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 0)
        password = "Dr0wss@p1_"
        response = self.client.post(
            f"{reverse('user-reset-password')}"
            f"?{urlencode({'token': token, 'username': 'username1'})}",
            {
                "password": password,
                "password_confirmation": password,
                "token": token,
                "username": "username1",
            },
        )
        self.assertEqual(
            len(fromstring(response.content).xpath("//*[text()='token not found']")),  # type: ignore[no-untyped-call]
            1,
        )

    def test_username_not_found(self) -> None:
        """Test username not found case."""
        token = token_urlsafe()
        cache.set("reset_user_password.username1", token, 600)
        password = "Dr0wss@p1_"
        response = self.client.post(
            f"{reverse('user-reset-password')}"
            f"?{urlencode({'token': token, 'username': 'username1'})}",
            {
                "password": password,
                "password_confirmation": password,
                "token": token,
                "username": "username1_",
            },
        )
        self.assertEqual(
            len(fromstring(response.content).xpath("//*[text()='username not found']")),  # type: ignore[no-untyped-call]
            1,
        )
