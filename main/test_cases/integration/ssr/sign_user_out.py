from django.urls import reverse
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class SignUserOutSsrTestCase(SsrTestCase):
    def test_get(self) -> None:
        """Test get form."""
        response = self.client.get(reverse("user-sign-out"))
        xpath = """
        //form
        [@method='post']
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        response = self.client.post(reverse("user-sign-out"))
        self.assertRedirects(response, reverse("user-sign-in"))
        client_session = self.client.cookies.get("sessionid")
        self.assertIsNone(client_session)
