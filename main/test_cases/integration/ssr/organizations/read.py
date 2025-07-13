from django.urls import reverse
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class ReadOrganizationsSsrTestCase(SsrTestCase):
    fixtures = ["organizations", "sessions", "users"]

    def test_get(self) -> None:
        """Test get page."""
        self.add_session_cookie()
        response = self.client.get(reverse("organizations-read", kwargs={"pk": 1}))
        html_element = fromstring(response.content)  # type: ignore[no-untyped-call]
        self.assertEqual(len(html_element.xpath(".//*[text()='code: code1']")), 1)
        self.assertEqual(len(html_element.xpath(".//*[text()='name: name1']")), 1)
