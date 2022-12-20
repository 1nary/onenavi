from django.views import View
from accounts.models import CustomUser
from .models import SaleItem
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from functools import reduce
from operator import and_

class SaleView(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    item_data = SaleItem.objects.all()
    params = {
      'user_data': user_data,
      'item_data': item_data,
    }
    return render(request, 'sale/sale.html', params)

class SaleSearchView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        keyword = request.GET.get('keyword')
        item_data = SaleItem.objects.filter(name__contains=keyword)
        params = {
          'user_data': user_data,
          'item_data': item_data,
          'keyword': keyword,
        }
        return render(request, 'sale/sale.html', params)


