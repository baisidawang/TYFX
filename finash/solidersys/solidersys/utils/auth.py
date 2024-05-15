from adminapp.models import RolePower, UserProfile, UserToken
from rest_framework import exceptions
from utils.encodeUtils import *
from django.db import connection


class AuthParam(object):
    def authenticate(self, request):
        sign = ""
        codingPwd = "Hb-Coding"
        if request.method == 'GET':
            qd = request.GET
        elif request.method == 'POST':
            qd = request.POST
        if len(qd) > 0:
            for k, v in qd.items():
                if k != 'sign':
                    sign += v
            sign+=codingPwd
            sign = signMd5(sign)
            if qd.get('sign', '*') != '*':
                if sign != qd['sign']:
                    raise exceptions.AuthenticationFailed('参数窜改!')
            else:
                raise exceptions.AuthenticationFailed('参数错误:无sign值!')
        else:
            raise exceptions.AuthenticationFailed('参数错误!')

    def authenticate_header(self, request):
        # 这个函数可以没有内容，但是必须得有
        pass


class Authtication(object):
    def authenticate(self, request):
        if request.method == 'GET':
            token = request.GET.get('token')
        elif request.method == 'POST':
            token = request.POST.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        # 这个函数可以没有内容，但是必须得有
        pass


class URLPerission(object):
    def has_permission(self, request, view):
        next_url = request.path_info
        # 找出token值--找出userid---找出roleid---找出apiurl
        # 三次数据库表访问，所以最好是写到存储过程里
        if request.method == 'GET':
            token = request.GET.get('token')
        elif request.method == 'POST':
            token = request.POST.get('token')

        #print(token,'token')
        #print("========")
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            return False
        #print(token,token_obj,'-----------------------',token_obj.user.id)
        userid = token_obj.user.id
        #====1
        user_obj = UserProfile.objects.filter(id=userid).first()
        can = RolePower.objects.filter(user_type=user_obj.user_type,canUrl=next_url).first()
        if can:
            return True
        else:
            return False
        #====2
        # cursor = connection.cursor()
        # cursor.callproc("proc_geturlFromUserid", (userid, next_url, 2))
        # result_list = []
        # for row in cursor.fetchall():
        #     result_list.append(row)
        # try:
        #     res = result_list[0][0]
        #     #print(userid, next_url, res)
        # # print("==========")
        # except:
        #     res = 0
        # finally:
        #     # connection.connection.commit()
        #     cursor.close()
        #     connection.close()
        # print('123123')
        # if res == 1:
        #     return True
        # else:
        #     return False


