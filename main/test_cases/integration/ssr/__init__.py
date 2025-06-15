from django.core.cache import cache
from django.test import TestCase
from lxml.html import HtmlElement


class SsrTestCase(TestCase):
    def add_session_cookie(self) -> None:
        """Add session cookie."""
        self.client.cookies["sessionid"] = "544vzd71puvnac7vyzermrtwjkwuq55w"

    def assert_table_body(
        self,
        actual_table_element: HtmlElement,
        expected_body_data: tuple[tuple[str, ...], ...],
    ) -> None:
        """Assert table body element with expected data wrapped in row tuples."""
        tr_elements = actual_table_element.xpath(".//tbody//tr")
        expected_row_count = len(expected_body_data)
        self.assertEqual(len(tr_elements), expected_row_count)
        for row_index in range(expected_row_count):
            expected_column_count = len(expected_body_data[row_index])
            for column_index in range(expected_column_count):
                self.assertEqual(
                    tr_elements[row_index].xpath(".//td")[column_index].text,
                    expected_body_data[row_index][column_index],
                )

    def assert_table_head(
        self, actual_table_element: HtmlElement, expected_header_data: tuple[str, ...]
    ) -> None:
        """Assert table head element."""
        th_elements = actual_table_element.xpath(".//thead//tr//th")
        expected_header_count = len(expected_header_data)
        self.assertEqual(len(th_elements), expected_header_count)
        for index in range(expected_header_count):
            self.assertEqual(th_elements[index].text, expected_header_data[index])

    def tearDown(self) -> None:
        """Clear cache."""
        cache.clear()
        super().tearDown()
