from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_params = 'page_size'
    max_page_size = 1000


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'link': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.page.paginator.count,
            'results': data
        })

    # def get_paginated_response_schema(self, schema):            
    #       return {
    #           'type': 'object',
    #           'properties': {
    #               'count': {
    #                   'type': 'integer',
    #                   'example': 123,
    #               },
    #               'next': {
    #                   'type': 'string',
    #                   'nullable': True,
    #                   'format': 'uri',
    #                   'example': 'http://api.example.org/accounts/? 
    #                       {page_query_param}=4'.format(
    #                       page_query_param=self.page_query_param)
    #               },
    #               'previous': {
    #                   'type': 'string',
    #                   'nullable': True,
    #                   'format': 'uri',
    #                   'example': 'http://api.example.org/accounts/? 
    #                       {page_query_param}=2'.format(
    #                       page_query_param=self.page_query_param)
    #               },                
    #               'page_size' : {
    #                   'type': 'integer',
    #                   'example': 123,
    #               },
    #               'total_pages': {
    #                   'type': 'integer',
    #                   'example': 123,
    #               },
    #               'current_page_number': {
    #                   'type': 'integer',
    #                   'example': 123,
    #               },
    #               'results': schema,
    #           },
    #       }