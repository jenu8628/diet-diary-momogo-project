from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import FoodSerializer
from .models import Food

# Create your views here.
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def foods_create(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_userFood(request, user_id):
    foods = Food.objects.filter(user_id=user_id)
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def foods_delete(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    serializer = FoodSerializer(food)
    food.delete()
    return Response(serializer.data)