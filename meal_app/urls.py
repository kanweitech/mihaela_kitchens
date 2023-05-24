from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/', views.meals_detail, name = "meals_detail"),
]