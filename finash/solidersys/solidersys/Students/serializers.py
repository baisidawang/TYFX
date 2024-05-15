from rest_framework import serializers
from Students.models import *

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User  # 修正这行，去掉括号
        fields = "__all__"