from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class ListOrganizationsSsrTestCase(SsrTestCase):
    fixtures = ["organizations", "sessions", "users"]

    def test_get(self) -> None:
        """Test get page."""
        self.add_session_cookie()
        response = self.client.get(reverse("organizations-list"))
        xpath = """
        .//table
            [.//thead//tr
                [.//th[text()='code']]
                [.//th[text()='name']]
            ]
            [.//tbody
                [.//tr
                    [.//td[text()='code1']]
                    [.//td[text()='name1']]
                ]
                [.//tr
                    [.//td[text()='code2']]
                    [.//td[text()='name2']]
                ]
            ]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_invalid_form(self) -> None:
        """Test submit invalid form."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'page_size': '_'})}"
        )
        xpath = """
        .//table
            [.//thead//tr
                [.//th[text()='code']]
                [.//th[text()='name']]
            ]
            [.//tbody[not(*)]]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_order(self) -> None:
        """Test paginating case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'sort_by': '-name'})}"
        )
        xpath = """
        .//table
            [.//thead//tr
                [.//th[text()='code']]
                [.//th[text()='name']]
            ]
            [.//tbody
                [.//tr
                    [.//td[text()='code2']]
                    [.//td[text()='name2']]
                ]
                [.//tr
                    [.//td[text()='code1']]
                    [.//td[text()='name1']]
                ]
            ]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_paginate(self) -> None:
        """Test ordering case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'page': 2, 'page_size': 1})}"
        )
        xpath = """
        .//table
            [.//thead//tr
                [.//th[text()='code']]
                [.//th[text()='name']]
            ]
            [.//tbody
                [.//tr
                    [.//td[text()='code2']]
                    [.//td[text()='name2']]
                ]
            ]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_filter_code_icontains(self) -> None:
        """Test filtering code-icontains case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'code__icontains': '2'})}"
        )
        xpath = """
        .//table
            [.//thead//tr
                [.//th[text()='code']]
                [.//th[text()='name']]
            ]
            [.//tbody
                [.//tr
                    [.//td[text()='code2']]
                    [.//td[text()='name2']]
                ]
            ]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_filter_name_icontains(self) -> None:
        """Test filtering name-icontains case."""
        self.add_session_cookie()
        response = self.client.get(
            f"{reverse('organizations-list')}?{urlencode({'name__icontains': '2'})}"
        )
        xpath = """
        .//table
            [.//thead//tr
                [.//th[text()='code']]
                [.//th[text()='name']]
            ]
            [.//tbody
                [.//tr
                    [.//td[text()='code2']]
                    [.//td[text()='name2']]
                ]
            ]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]
