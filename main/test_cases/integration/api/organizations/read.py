from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class ReadOrganizationsApiTestCase(ApiTestCase):
    fixtures = ["organizations", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(
            reverse("api-organizations-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        self.client.force_authenticate(user=User.objects.get(pk=1))
        response = self.client.get(
            reverse("api-organizations-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json(), {"code": "code1", "name": "name1"})
