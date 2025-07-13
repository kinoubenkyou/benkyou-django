from django.urls import reverse
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class ReadUserSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_get(self) -> None:
        """Test get page."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-read"))
        html_element = fromstring(response.content)  # type: ignore[no-untyped-call]
        self.assert_match_once(html_element, ".//*[text()='username: username1']")
        self.assert_match_once(html_element, ".//*[text()='email: email1@email.com']")
        self.assert_match_once(html_element, ".//*[text()='email_is_verified: False']")
