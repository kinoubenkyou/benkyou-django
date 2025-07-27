from django.core.cache import cache
from rest_framework.test import APIClient
from rest_framework.test import APITestCase as RestFrameworkAPITestCase


class ApiTestCase(RestFrameworkAPITestCase):
    client: APIClient

    def tearDown(self) -> None:
        """Clear cache."""
        cache.clear()
        return super().tearDown()
