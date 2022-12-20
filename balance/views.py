from django.views import View
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class BalanceView(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    params = {
      'user_data': user_data,
    }
    return render(request, 'balance/balance.html', params)