from rest_framework import pagination

from core.api.api_responses import SuccessAPIResponse


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return SuccessAPIResponse({
            "total_pages": self.page.paginator.num_pages,
            "total_items": self.page.paginator.count,
            "current_page": self.page.number,
            "next": self.get_next_link(),
            "previous": self.get_previous_link()
        })
