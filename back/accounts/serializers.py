from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'nickname', 'password','age','height', 'weight', 'sex','passwordconfirm')
        # read_only_fields = ('password')