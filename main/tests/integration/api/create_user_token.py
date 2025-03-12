from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK

from main.tests.integration.api import ApiTestCase


class CreateUserTokenApiTestCase(ApiTestCase):
    fixtures = ["user"]

    def test(self) -> None:
        """Test success case."""
        response = self.client.post(
            reverse("api-user-token"),
            data={"username": "username1", "password": "Dr0wss@p1"},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        token = Token.objects.filter(user=1).first()
        self.assertIsNotNone(token)
        self.assertEqual(response.json()["token"], token.key)  # type: ignore[union-attr]
