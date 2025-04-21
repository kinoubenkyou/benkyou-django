from django.core.cache import cache
from django.test import TestCase


class SsrTestCase(TestCase):
    def add_session_cookie(self) -> None:
        """Add session cookie."""
        self.client.cookies["sessionid"] = "544vzd71puvnac7vyzermrtwjkwuq55w"

    def tearDown(self) -> None:
        """Clear cache."""
        cache.clear()
        super().tearDown()
