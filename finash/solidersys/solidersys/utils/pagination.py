from rest_framework.pagination import  PageNumberPagination

class MyPagination(PageNumberPagination):
    """自定义分页"""
    # 每页显示多少条数据
    page_size = 6
    # url/?page=1&size=5, 改变默认每页显示的个数
    page_size_query_param = "size"
    # 最大页数不超过10条
    max_page_size = 10
    # 获取页码数
    page_query_param = "page"
