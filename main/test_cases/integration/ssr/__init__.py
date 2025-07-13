from django.core.cache import cache
from django.test import TestCase
from lxml.html import HtmlElement


class SsrTestCase(TestCase):
    def add_session_cookie(self) -> None:
        """Add session cookie."""
        self.client.cookies["sessionid"] = "544vzd71puvnac7vyzermrtwjkwuq55w"

    def assert_match_once(self, html_element: HtmlElement, xpath: str) -> None:
        """Assert an HTML element matches xpath once."""
        self.assertEqual(len(html_element.xpath(xpath)), 1)

    def tearDown(self) -> None:
        """Clear cache."""
        cache.clear()
        super().tearDown()
