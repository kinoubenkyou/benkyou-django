from django.conf import settings
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.fixtures.session_id import SessionId
from main.test_cases.integration.ssr import SsrTestCase


class ReadOrganizationSsrTestCase(SsrTestCase):
    fixtures = ["organizations", "organizationusers", "sessions", "users"]

    def test_get(self) -> None:
        """Test get page."""
        self.client.cookies[settings.SESSION_COOKIE_NAME] = (
            SessionId.SWITCHED_ORGANIZATION
        )
        response = self.client.get(reverse("organization-read"))
        html_element = fromstring(response.content)  # type: ignore[no-untyped-call]
        self.assertEqual(len(html_element.xpath(".//*[text()='code: code1']")), 1)
        self.assertEqual(len(html_element.xpath(".//*[text()='name: name1']")), 1)

    def test_switched_organization_required(self) -> None:
        """Test switched organization required."""
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
        response = self.client.get(reverse("organization-read"))
        self.assertRedirects(
            response,
            f"{reverse('organization-switch')}"
            f"?{urlencode({'next': reverse('organization-read')})}",
        )
