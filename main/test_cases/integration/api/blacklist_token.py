from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class BlacklistTokenApiTestCase(ApiTestCase):
    fixtures = ["users"]

    def test(self) -> None:
        """Test success case."""
        refresh_token = RefreshToken.for_user(User.objects.get(pk=1))
        response = self.client.post(
            reverse("api-blacklist-token"), data={"refresh": refresh_token}
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertTrue(
            BlacklistedToken.objects.filter(token__jti=refresh_token["jti"]).exists()
        )
