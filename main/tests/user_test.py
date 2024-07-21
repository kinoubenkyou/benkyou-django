from django.test import TestCase

from main.models import User


class UserTest(TestCase):
    fixtures = ["user"]

    def test_get_absolute_url(self):
        object_ = User.objects.get(pk=1)

        actual = object_.get_absolute_url()

        self.assertEqual(actual, "/users/1/")
