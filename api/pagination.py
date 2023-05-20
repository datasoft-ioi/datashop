from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPaagination(PageNumberPagination):
    def get_paginated_response(self, data):
        response = Response({
            'link': {
                "Keyingi": self.get_next_link(),
                "Oldingi": self.get_previous_link()
            },
            "count": self.page.paginator.count,
            "results": data

        })
        return response