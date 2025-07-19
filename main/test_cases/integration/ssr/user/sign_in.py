from django.conf import settings
from django.contrib.sessions.models import Session
from django.urls import reverse
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class SignUserInSsrTestCase(SsrTestCase):
    fixtures = ["users"]

    def test_get(self) -> None:
        """Test get form."""
        response = self.client.get(reverse("user-sign-in"))
        xpath = """
        //form
            [@method='post']
            [//input[@name='username']]
            [//input[@name='password']]
            [//input[@type='submit']]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        username = "username1"
        password = "Dr0wss@p1"
        response = self.client.post(
            reverse("user-sign-in"), {"username": username, "password": password}
        )
        self.assertRedirects(response, reverse("user-read"))
        client_session = self.client.cookies.get(settings.SESSION_COOKIE_NAME)
        self.assertIsNotNone(client_session)
        server_session = Session.objects.get(pk=client_session.value)  # type: ignore[union-attr]
        self.assertEqual(server_session.get_decoded()["_auth_user_id"], "1")
