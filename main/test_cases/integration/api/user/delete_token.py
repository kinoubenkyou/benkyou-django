from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT

from main.test_cases.integration.api import ApiTestCase


class DeleteUserTokenApiTestCase(ApiTestCase):
    fixtures = ["tokens", "users"]

    def test(self) -> None:
        """Test success case."""
        self.add_authentication_token()
        response = self.client.delete(reverse("api-user-token"))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Token.objects.filter(user=1).exists())
