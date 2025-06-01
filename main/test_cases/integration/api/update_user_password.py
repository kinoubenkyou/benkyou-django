from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)

from main.models import User
from main.test_cases.integration.api import ApiTestCase


class UpdateUserPasswordApiTestCase(ApiTestCase):
    fixtures = ["user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.post(reverse("api-user-update-password"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test(self) -> None:
        """Test success case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        new_password = "Dr0wss@p01"
        response = self.client.post(
            reverse("api-user-update-password"),
            data={"old_password": "Dr0wss@p1", "new_password": new_password},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        user.refresh_from_db()
        self.assertTrue(user.check_password(new_password))

    def test__incorrect_old_password(self) -> None:
        """Test incorrect old password case."""
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        response = self.client.post(
            reverse("api-user-update-password"),
            data={"old_password": "Dr0wss@p1_", "new_password": "Dr0wss@p01"},
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"old_password": ["incorrect old password"]})
