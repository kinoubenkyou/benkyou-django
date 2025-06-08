from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class UpdateUserPasswordSsrTestCase(SsrTestCase):
    fixtures = ["session", "user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("user-update-password"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}"
            f"?{urlencode({'next': reverse('user-update-password')})}",
        )

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-update-password"))
        xpath = """
        //form
        [@method='post']
        [//input[@name='old_password']]
        [//input[@name='new_password']]
        [//input[@name='new_password_confirmation']]
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        password = "Dr0wss@p01"
        response = self.client.post(
            reverse("user-update-password"),
            {
                "old_password": "Dr0wss@p1",
                "new_password": password,
                "new_password_confirmation": password,
            },
        )
        self.assertRedirects(response, reverse("user-read"))
        self.assertTrue(User.objects.get(pk=1).check_password(password))

    def test__incorrect_old_password(self) -> None:
        """Test incorrect old password case."""
        self.add_session_cookie()
        password = "Dr0wss@p01"
        response = self.client.post(
            reverse("user-update-password"),
            {
                "old_password": "Dr0wss@p1_",
                "new_password": password,
                "new_password_confirmation": password,
            },
        )
        self.assertEqual(
            len(
                fromstring(response.content).xpath(  # type: ignore[no-untyped-call]
                    "//*[text()='incorrect old password']"
                )
            ),
            1,
        )
