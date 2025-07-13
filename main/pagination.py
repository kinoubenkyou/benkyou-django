from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    max_page_size = 100
    page_size = 50
    page_size_query_param = "page_size"
