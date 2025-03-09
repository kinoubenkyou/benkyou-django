from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APILiveServerTestCase


class GetUserTokenApiTestCase(APILiveServerTestCase):
    fixtures = ["user"]  # type: ignore[assignment]

    def test(self) -> None:
        """Test success case."""
        response = self.client.post(
            reverse("api-user-get-token"),
            data={"username": "username1", "password": "Dr0wss@p1"},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        token = Token.objects.filter(user=1).first()  # type: ignore[attr-defined]
        self.assertIsNotNone(token)
        self.assertEqual(response.json()["token"], token.key)
