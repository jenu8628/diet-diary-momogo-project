from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('password/', views.password_confirm),
    path('api-token-auth/', obtain_jwt_token),
    path('myprofile/', views.my_profile),
    path('update/', views.update),
]