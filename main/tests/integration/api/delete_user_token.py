from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from main.tests.integration.api import ClientTestCase


class DeleteUserTokenApiTestCase(ClientTestCase):
    fixtures = ["token", "user"]  # type: ignore[assignment]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.delete(reverse("api-user-token"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        self.add_authentication_token()
        response = self.client.delete(reverse("api-user-token"))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Token.objects.filter(user=1).exists())  # type: ignore[attr-defined]
