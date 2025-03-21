from django.core.cache import cache
from rest_framework.test import APIClient, APITestCase


class ApiTestCase(APITestCase):
    client: APIClient

    def add_authentication_token(self) -> None:
        """Add authentication token."""
        self.client.credentials(
            HTTP_AUTHORIZATION="Token 703f63305242864e94b7937af0dd7a4976f05b20"
        )

    def tearDown(self) -> None:
        """Clear cache."""
        cache.clear()
        return super().tearDown()
