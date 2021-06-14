from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import User

@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordconfirm')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def password_confirm(request):
    new_dict = {
      'password' : request.user.passwordconfirm
    }
    return Response(new_dict)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)
    return Response(serializer.data)
    


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request):
    # print(request.data.get('user_id'))
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    # print(request.data.get('user_info'))
    update_user_serializer = UserSerializer(user, data=request.data.get('user_info'))
    # print(update_user_serializer.is_valid())
    # print(update_user_serializer.errors)
    if update_user_serializer.is_valid():
        update_user_serializer.save()
        return Response(update_user_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)