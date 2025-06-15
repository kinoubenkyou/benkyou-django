from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class ListOrganizationsSsrTestCase(SsrTestCase):
    fixtures = ["organizations", "sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("organizations-list"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}"
            f"?{urlencode({'next': reverse('organizations-list')})}",
        )

    def test_get(self) -> None:
        """Test get page."""
        self.add_session_cookie()
        response = self.client.get(reverse("organizations-list"))
        table_elements = fromstring(response.content).xpath(".//table")  # type: ignore[no-untyped-call]
        self.assertEqual(len(table_elements), 1)
        self.assert_table_head(table_elements[0], ("code", "name"))
        self.assert_table_body(
            table_elements[0], (("code1", "name1"), ("code2", "name2"))
        )

    def test_invalid_form(self) -> None:
        """Test submit invalid form."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'page_size': '_'})}"
        )
        table_elements = fromstring(response.content).xpath(".//table")  # type: ignore[no-untyped-call]
        self.assertEqual(len(table_elements), 1)
        self.assert_table_body(table_elements[0], tuple())

    def test_order(self) -> None:
        """Test paginating case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'sort_by': '-name'})}"
        )
        table_elements = fromstring(response.content).xpath(".//table")  # type: ignore[no-untyped-call]
        self.assertEqual(len(table_elements), 1)
        self.assert_table_body(
            table_elements[0], (("code2", "name2"), ("code1", "name1"))
        )

    def test_paginate(self) -> None:
        """Test ordering case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'page': 2, 'page_size': 1})}"
        )
        table_elements = fromstring(response.content).xpath(".//table")  # type: ignore[no-untyped-call]
        self.assertEqual(len(table_elements), 1)
        self.assert_table_body(table_elements[0], (("code2", "name2"),))

    def test_filter_code_icontains(self) -> None:
        """Test filtering code-icontains case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'code__icontains': '2'})}"
        )
        table_elements = fromstring(response.content).xpath(".//table")  # type: ignore[no-untyped-call]
        self.assertEqual(len(table_elements), 1)
        self.assert_table_body(table_elements[0], (("code2", "name2"),))

    def test_filter_name_icontains(self) -> None:
        """Test filtering name-icontains case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'name__icontains': '2'})}"
        )
        table_elements = fromstring(response.content).xpath(".//table")  # type: ignore[no-untyped-call]
        self.assertEqual(len(table_elements), 1)
        self.assert_table_body(table_elements[0], (("code2", "name2"),))
