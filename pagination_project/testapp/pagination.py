from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

# Create your views here.
class Mypagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage'
    page_size_query_param = 'num'

class Myoffset(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 20