from django.urls import path
from sub_app import views


urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name = "drink_name")
]