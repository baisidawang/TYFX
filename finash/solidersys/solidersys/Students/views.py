from rest_framework.views import APIView
from rest_framework.response import Response
from utils.responseUtils import *
from utils.utilModel import Param
from Students.serializers import *

class GetUserView(APIView):
  authentication_classes=[]
  permission_classes=[]
  def get(self,request,format=None):
    param = Param()
    param.add('student_id', request.GET.get('student_id'), 'like')
    param.add('password', request.GET.get('password'), 'eq')
    filter_dict = param.create()
    _data = User.objects.filter(**filter_dict)
    _data_serializer=UserSerializer(_data,many=True)
    return Response(_data_serializer.data)

class Add_info(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        id = request.POST.get('id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        nation = request.POST.get('nation')
        birthday = request.POST.get('birthday')
        politic = request.POST.get('politic')
        Sno = request.POST.get('Sno')
        domicile = request.POST.get('domicile')
        ID_card = request.POST.get('ID_card')
        enlist_time = request.POST.get('enlist_time')
        retire_time = request.POST.get('retire_time')
        before_teacher = request.POST.get('before_teacher')
        retire_teacher = request.POST.get('retire_teacher')
        before_class = request.POST.get('before_class')
        retire_class = request.POST.get('retire_class')
        searvice_troops = request.POST.get('searvice_troops')
        duties = request.POST.get('duties')
        number = request.POST.get('number')
        family_number = request.POST.get('family_number')
        enlist_place = request.POST.get('enlist_place')
        pend = request.POST.get('pend')
        rewards = request.POST.get('rewards')
        certifiate = request.POST.get('certifiate')
        personal_photo = request.POST.get('personal_photo')
        enlist_photo = request.POST.get('enlist_photo')
        retire_photo = request.POST.get('retire_photo')
        sign_photo = request.POST.get('sign_photo')
        isValid = 1
        basicinfo = BasicInfo()
        if not (id == '' or id == None):
            basicinfo.id = id
        basicinfo.name = name
        basicinfo.gender = gender
        basicinfo.nation = nation
        basicinfo.birthday = birthday
        basicinfo.politic = politic
        basicinfo.Sno = Sno
        basicinfo.domicile = domicile
        basicinfo.ID_card = ID_card
        basicinfo.enlist_time = enlist_time
        basicinfo.retire_time = retire_time
        basicinfo.before_teacher = before_teacher
        basicinfo.retire_teacher = retire_teacher
        basicinfo.before_class = before_class
        basicinfo.retire_class = retire_class
        basicinfo.searvice_troops = searvice_troops
        basicinfo.duties = duties
        basicinfo.number = number
        basicinfo.family_number = family_number
        basicinfo.enlist_place = enlist_place
        basicinfo.pend = pend
        basicinfo.rewards = rewards
        basicinfo.certifiate = certifiate
        basicinfo.personal_photo =personal_photo
        basicinfo.enlist_photo = enlist_photo
        basicinfo.retire_photo = retire_photo
        basicinfo.sign_photo = sign_photo
        basicinfo.isValid = isValid
        basicinfo.save()
        return responseJson('添加成功', '200')

class Query_info(APIView):
  def get(self,request,format=None):
    param = Param()
    param.add('isValid',1, 'eq')
    param.add('Sno', request.GET.get('sno'), 'eq')
    param.add('ID_card', request.GET.get('id_card'), 'eq')
    param.add('name', request.GET.get('searchWord'), 'like')
    filter_dict = param.create()
    _data = BasicInfo.objects.filter(**filter_dict)
    _data_serializer=BasicInfoSerializer(_data,many=True)
    result = {
      "data":_data_serializer.data
    }
    return Response(result)

class Delet_info(APIView):
  #下面这两项可以让请求不用携带token值
  authentication_classes=[]
  permission_classes=[]
  def post(self,request,format=None):
    id = request.POST.get('id')
    if  id == '' or id == None:
      return responseJson('编号有误', 'fail')
    else:
      try:
        basicinfo=BasicInfo.objects.get(pk=id)
        # basicinfo.isValid = 0
        basicinfo.delete()
        return responseJson('删除成功', '200')
      except BasicInfo.DoesNotExist:
          return responseJson('未找到匹配的数据', 404)
      except Exception as e:
          return responseJson('删除失败', 500)
      # except:
      #   return responseJson('删除失败',505)

  # def post(self, request, format=None):
  #     sno = request.POST.get('sno')
  #     if sno == '' or sno is None:
  #         return Response({'message': '学号不能为空'}, status=400)
  #
  #     try:
  #         basic_info = BasicInfo.objects.get(Sno=sno)
  #         basic_info.delete()
  #         return Response({'message': '删除成功'}, status=200)
  #     except BasicInfo.DoesNotExist:
  #         return Response({'message': '学号不存在，无法删除'}, status=404)
  #     except Exception as e:
  #         return Response({'message': '删除失败', 'error': str(e)}, status=500)

###这个是针对微信小程序的上传方法
class Add(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        id = request.data.get('id')
        name = request.data.get('name')
        gender = request.data.get('gender')
        nation = request.data.get('nation')
        birthday = request.data.get('birthday')
        politic = request.data.get('politic')
        Sno = request.data.get('Sno')
        domicile = request.data.get('domicile')
        ID_card = request.data.get('ID_card')
        enlist_time = request.data.get('enlist_time')
        retire_time = request.data.get('retire_time')
        before_teacher = request.data.get('before_teacher')
        retire_teacher = request.data.get('retire_teacher')
        before_class = request.data.get('before_class')
        retire_class = request.data.get('retire_class')
        searvice_troops = request.data.get('searvice_troops')
        duties = request.data.get('duties')
        number = request.data.get('number')
        family_number = request.data.get('family_number')
        enlist_place = request.data.get('enlist_place')
        pend = request.data.get('pend')
        rewards = request.data.get('rewards')
        certifiate = request.data.get('certifiate')
        personal_photo = request.data.get('personal_photo')
        enlist_photo = request.data.get('enlist_photo')
        retire_photo = request.data.get('retire_photo')
        sign_photo = request.data.get('sign_photo')
        isValid = 1
        basicinfo = BasicInfo()
        if not (id == '' or id == None):
            basicinfo.id = id
        basicinfo.name = name
        basicinfo.gender = gender
        basicinfo.nation = nation
        basicinfo.birthday = birthday
        basicinfo.politic = politic
        basicinfo.Sno = Sno
        basicinfo.domicile = domicile
        basicinfo.ID_card = ID_card
        basicinfo.enlist_time = enlist_time
        basicinfo.retire_time = retire_time
        basicinfo.before_teacher = before_teacher
        basicinfo.retire_teacher = retire_teacher
        basicinfo.before_class = before_class
        basicinfo.retire_class = retire_class
        basicinfo.searvice_troops = searvice_troops
        basicinfo.duties = duties
        basicinfo.number = number
        basicinfo.family_number = family_number
        basicinfo.enlist_place = enlist_place
        basicinfo.pend = pend
        basicinfo.rewards = rewards
        basicinfo.certifiate = certifiate
        basicinfo.personal_photo =personal_photo
        basicinfo.enlist_photo = enlist_photo
        basicinfo.retire_photo = retire_photo
        basicinfo.sign_photo = sign_photo
        basicinfo.isValid = isValid
        basicinfo.save()
        return responseJson('添加成功', '200')