from django.views import View
from accounts.models import CustomUser
from .models import SaleItem, SaleFavorite
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from functools import reduce
from operator import and_

class SaleView(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    item_data = SaleItem.objects.all()
    favorite_list = []
    for data in item_data:
      favorite = data.salefavorite_set.filter(user=request.user)
      if favorite.exists():
        favorite_list.append(data.id)
    params = {
      'user_data': user_data,
      'item_data': item_data,
      'favorite_list': favorite_list,
    }
    return render(request, 'sale/sale.html', params)

class SaleSearchView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        keyword = request.GET.get('keyword')
        item_data = SaleItem.objects.filter(name__contains=keyword)
        favorite_list = []
        for data in item_data:
          favorite = data.salefavorite_set.filter(user=request.user)
          if favorite.exists():
            favorite_list.append(data.id)
        
        params = {
          'user_data': user_data,
          'item_data': item_data,
          'keyword': keyword,
          'favorite_list': favorite_list,
        }
        return render(request, 'sale/sale.html', params)


