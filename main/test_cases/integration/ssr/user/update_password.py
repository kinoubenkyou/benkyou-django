from django.urls import reverse
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class UpdateUserPasswordSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-update-password"))
        xpath = """
        .//form
            [@method='post']
            [.//input[@name='old_password']]
            [.//input[@name='new_password']]
            [.//input[@name='new_password_confirmation']]
            [.//input[@type='submit']]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        password = "Dr0wss@p1_"
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

    def test_incorrect_old_password(self) -> None:
        """Test incorrect old password case."""
        self.add_session_cookie()
        password = "Dr0wss@p1_"
        response = self.client.post(
            reverse("user-update-password"),
            {
                "old_password": "Dr0wss@p1_",
                "new_password": password,
                "new_password_confirmation": password,
            },
        )
        self.assert_match_once(
            fromstring(response.content),  # type: ignore[no-untyped-call]
            ".//*[text()='incorrect old password']",
        )

    def test_new_password_and_confirmation_not_match(self) -> None:
        """Test incorrect password and confirmation not match case."""
        self.add_session_cookie()
        password = "Dr0wss@p1_"
        response = self.client.post(
            reverse("user-update-password"),
            {
                "old_password": "Dr0wss@p1",
                "new_password": password,
                "new_password_confirmation": f"{password}_",
            },
        )
        self.assert_match_once(
            fromstring(response.content),  # type: ignore[no-untyped-call]
            ".//*[text()='new password and confirmation not match']",
        )
