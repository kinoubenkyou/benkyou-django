from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase


class GetUserTokenApiTestCase(APILiveServerTestCase):
    fixtures = ["user"]  # type: ignore[assignment]

    def test(self) -> None:
        """Test success case."""
        response = self.client.post(
            reverse("api-user-get-token"),
            data={"username": "username1", "password": "Dr0wss@p1"},
        )
        self.assertEqual(Token.objects.get(key=response.json()["token"]).user.id, 1)  # type: ignore[attr-defined]
