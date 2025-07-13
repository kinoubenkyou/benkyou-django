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
        self.assertEqual(
            len(html_element.xpath(".//*[text()='username: username1']")), 1
        )
        self.assertEqual(
            len(html_element.xpath(".//*[text()='email: email1@email.com']")), 1
        )
        self.assertEqual(
            len(html_element.xpath(".//*[text()='email_is_verified: False']")), 1
        )
