from django.http import Http404
from django.test import SimpleTestCase, RequestFactory

from main.views import UserDeleteView, UserListView


class UserDeleteViewTest(SimpleTestCase):
    def test_get(self):
        object_ = UserDeleteView()

        with self.assertRaises(Http404):
            object_.get(None)

    def test_get_success_url(self):
        object_ = UserDeleteView()

        actual = object_.get_success_url()

        self.assertEqual(actual, "/users/")


class UserListViewTest(SimpleTestCase):
    def test_get_context_data(self):
        object_ = UserListView()
        object_.setup(
            RequestFactory().get("/users?email__icontains=email&name__icontains=name")
        )
        object_.object_list = []

        actual = object_.get_context_data()

        self.assertIn("email__icontains", actual)
        self.assertEqual(actual["email__icontains"], "email")
        self.assertIn("name__icontains", actual)
        self.assertEqual(actual["name__icontains"], "name")

    def test_get_queryset(self):
        object_ = UserListView()
        object_.setup(
            RequestFactory().get("/users?email__icontains=email&name__icontains=name")
        )

        actual = object_.get_queryset()

        self.assertIn(
            'UPPER("main_user"."email"::text) LIKE UPPER(%email%)',
            actual.query.__str__(),
        )
        self.assertIn(
            'UPPER("main_user"."name"::text) LIKE UPPER(%name%)', actual.query.__str__()
        )
