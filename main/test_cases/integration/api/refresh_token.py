from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class RefreshTokenApiTestCase(ApiTestCase):
    fixtures = ["users"]

    def test(self) -> None:
        """Test success case."""
        response = self.client.post(
            reverse("api-refresh-token"),
            data={"refresh": RefreshToken.for_user(User.objects.get(pk=1))},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(AccessToken(response.json()["access"])["user_id"], "1")
