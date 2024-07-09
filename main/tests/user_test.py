from unittest import TestCase

from main.models import User


class UserTest(TestCase):
    def test_get_absolute_url(self):
        object_ = User()
        object_.pk = 1

        actual = object_.get_absolute_url()

        self.assertEqual(actual, '/users/1/')
