from rest_framework import serializers
from .models import Food
from accounts.serializers import UserSerializer

class FoodSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Food
        fields = ('id','user', 'time', 'foodName', 'amount', 'kcal', 'carbohydrate', 'protein', 'fat','unit','natrium', 'sugars', 'created_at',)