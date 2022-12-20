from django.urls import path
from menu import views

urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='menu_top'),
]