from django.utils.http import urlencode
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class ListOrganizationsApiTestCase(ApiTestCase):
    fixtures = ["organizations", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("api-organizations-list"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(reverse("api-organizations-list"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.json()["results"],
            [
                {"code": "code1", "name": "name1"},
                {"code": "code2", "name": "name2"},
            ],
        )

    def test_order(self) -> None:
        """Test paginating case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(
            f"{reverse('api-organizations-list')}?{urlencode({'sort_by': '-name'})}"
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.json()["results"],
            [
                {"code": "code2", "name": "name2"},
                {"code": "code1", "name": "name1"},
            ],
        )

    def test_paginate(self) -> None:
        """Test ordering case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(
            f"{reverse('api-organizations-list')}"
            f"?{urlencode({'page': 2, 'page_size': 1})}"
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.json()["results"],
            [
                {"code": "code2", "name": "name2"},
            ],
        )

    def test_filter_code_icontains(self) -> None:
        """Test filtering code-icontains case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(
            f"{reverse('api-organizations-list')}?{urlencode({'code__icontains': '2'})}"
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.json()["results"],
            [
                {"code": "code2", "name": "name2"},
            ],
        )

    def test_filter_name_icontains(self) -> None:
        """Test filtering name-icontains case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(
            f"{reverse('api-organizations-list')}?{urlencode({'name__icontains': '2'})}"
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.json()["results"],
            [
                {"code": "code2", "name": "name2"},
            ],
        )
