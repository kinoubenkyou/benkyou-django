from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class ReadOrganizationsSsrTestCase(SsrTestCase):
    fixtures = ["organizations", "sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("organizations-read", kwargs={"pk": 1}))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}"
            f"?{urlencode({'next': reverse('organizations-read', kwargs={'pk': 1})})}",
        )

    def test_get(self) -> None:
        """Test get page."""
        self.add_session_cookie()
        response = self.client.get(reverse("organizations-read", kwargs={"pk": 1}))
        html_element = fromstring(response.content)  # type: ignore[no-untyped-call]
        self.assert_match_once(html_element, ".//*[text()='code: code1']")
        self.assert_match_once(html_element, ".//*[text()='name: name1']")
