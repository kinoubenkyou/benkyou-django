from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class UpdateUserSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("user-update"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}?{urlencode({'next': reverse('user-update')})}",
        )

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-update"))
        xpath = """
        //form
        [@method='post']
        [//input[@name='email']]
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        username = "username1_"
        email = "email01@email.com"
        response = self.client.post(
            reverse("user-update"),
            {
                "username": username,
                "email": email,
            },
        )
        self.assertRedirects(response, reverse("user-read"))
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
