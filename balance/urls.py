from django.urls import path
from balance import views

urlpatterns = [
    path('balance/', views.BalanceView.as_view(), name='balance_top'),
]