from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('signin/', views.LoginView.as_view(), name='account_signin'),
    path('logout/', views.LogoutView, name='account_logout'),
    path('mypage/', views.MypageView.as_view(), name='account_mypage'),
]