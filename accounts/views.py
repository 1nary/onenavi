from django.views import View
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from allauth.account import views
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib import request
from django.contrib.auth import login,logout
from accounts.forms import SignupUserForm

class LoginView(views.LoginView):
  template_name = 'accounts/signin.html'

class MypageView(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    return render(request, 'accounts/mypage.html', {
      'user_data': user_data,
    })

class SignupView(views.SignupView):
  template_name = 'accounts/signup.html'
  form_class = SignupUserForm

def LogoutView(request):
    logout(request) 
    return redirect(to='/accounts/signin/')
