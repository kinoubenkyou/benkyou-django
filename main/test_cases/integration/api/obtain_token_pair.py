from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from main.test_cases.integration.api import ApiTestCase


class ObtainTokenPairApiTestCase(ApiTestCase):
    fixtures = ["users"]

    def test(self) -> None:
        """Test success case."""
        response = self.client.post(
            reverse("api-obtain-token-pair"),
            data={"username": "username1", "password": "Dr0wss@p1"},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertEqual(AccessToken(data["access"])["user_id"], "1")
        self.assertEqual(RefreshToken(data["refresh"])["user_id"], "1")
