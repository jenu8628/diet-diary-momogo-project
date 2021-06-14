from django.db import models
from django.conf import settings

# Create your models here.

class Food(models.Model):
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='food',
  )
  # 아침, 점심, 저녁, 간식
  time = models.TextField(default="아침")
  # 음식 이름
  foodName = models.TextField()
  # 용량
  amount = models.IntegerField()
  # 칼로리
  kcal = models.IntegerField()
  # 탄수화물
  carbohydrate = models.IntegerField()
  # 단백질
  protein = models.IntegerField()
  # 지방
  fat = models.IntegerField()
  # 단위
  unit = models.TextField()
  # 나트륨
  natrium = models.IntegerField()
  # 당류
  sugars = models.IntegerField()
  # 생성시간
  created_at = models.DateTimeField(auto_now_add=True)