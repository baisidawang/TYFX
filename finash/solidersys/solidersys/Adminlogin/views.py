import json
from rest_framework.views import APIView
from Adminlogin.models import *
from utils.responseUtils import *

# class GetUserView(APIView):
#   authentication_classes=[]
#   permission_classes=[]
#   def get(self,request,format=None):
#     param = Param()
#     param.add('student_id', request.GET.get('student_id'), 'like')
#     param.add('password', request.GET.get('password'), 'eq')
#     filter_dict = param.create()
#     _data = User.objects.filter(**filter_dict)
#     _data_serializer=UserSerializer(_data,many=True)
#     return Response(_data_serializer.data)

# class GetUserView(APIView):
#   authentication_classes=[]
#   permission_classes=[]
#   def get(self,request,format=None):
#     param = Param()
#     param.add('student_id', request.GET.get('student_id'), 'like')
#     param.add('password', request.GET.get('password'), 'eq')
#     filter_dict = param.create()
#     _data = User.objects.filter(**filter_dict)
#     _data_serializer=UserSerializer(_data,many=True)
#     return Response(_data_serializer.data)
#
# class Login(APIView):
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = CustomUser.objects.filter(username=username, password=password)
#         if user is not None:
#             data = {'success': True}
#             return responseJson('登陆成功', '200', data)
#         else:
#             data = {'success': False}
#             return responseJson('用户名或密码错误', '403', data)
