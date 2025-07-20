from urllib.parse import urlencode

from django.conf import settings
from django.contrib.sessions.models import Session
from django.urls import reverse
from lxml.html import fromstring

from main.fixtures.session_id import SessionId
from main.test_cases.integration.ssr import SsrTestCase


class SwitchOrganizationSsrTestCase(SsrTestCase):
    fixtures = ["organizations", "organizationusers", "sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("user-update"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}?{urlencode({'next': reverse('user-update')})}",
        )

    def test_get(self) -> None:
        """Test get form."""
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
        response = self.client.get(reverse("organization-switch"))
        xpath = """
                .//form
                    [@method='post']
                    [.//select
                        [@name='organization']
                        [.//option
                            [@value='1']
                            [text()='name1']
                        ]
                        [.//option
                            [@value='2']
                            [text()='name2']
                        ]
                    ]
                    [.//input[@type='submit']]
                """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
        response = self.client.post(
            reverse("organization-switch"), {"organization": "1"}
        )
        self.assertRedirects(response, reverse("user-read"))
        client_session = self.client.cookies.get(settings.SESSION_COOKIE_NAME)
        self.assertIsNotNone(client_session)
        server_session = Session.objects.get(pk=client_session.value)  # type: ignore[union-attr]
        self.assertEqual(server_session.get_decoded().get("organization_id"), 1)
