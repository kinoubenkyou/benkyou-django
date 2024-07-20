from django.test import SimpleTestCase

from main.views import UserDeleteView


class UserDeleteViewTest(SimpleTestCase):
    def test_get_success_url(self):
        object_ = UserDeleteView()

        actual = object_.get_success_url()

        self.assertEqual(actual, "/users/")
