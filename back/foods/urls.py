from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods_create),
    path('<int:user_id>/get_userFood/', views.get_userFood),
    path('<int:food_id>/delete/', views.foods_delete),
]
