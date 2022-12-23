from django.views import View
from accounts.models import CustomUser
from .models import SaleItem, SaleFavorite
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

class SaleView(LoginRequiredMixin,View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    item_data = SaleItem.objects.all()
    favorite_list = []
    shop = []
    for data in item_data:
      favorite = data.salefavorite_set.filter(user=request.user)
      if favorite.exists():
        favorite_list.append(data.id)

    if user_data.address == '沖縄県':
      shop = ['サンエー','イオン','りうぼう']
    
    params = {
      'user_data': user_data,
      'item_data': item_data,
      'favorite_list': favorite_list,
      'shop': shop
    }
    return render(request, 'sale/sale.html', params)

def SaleFavoriteView(request):
  user = request.user
  if request.method == 'POST':
    item_id = request.POST.get('item_id')
    item_data = SaleItem.objects.get(id=item_id)
    item_data_favorite = SaleFavorite.objects.filter(saleitem=item_data)
    favorited = False

    if item_data_favorite:
      item_data_favorite.delete()
    else:
      item_data_favorite.create(saleitem=item_data, user=user)
      favorited = True
    params = {
      'item_id': item_data.id,
      'favorited': favorited,
    }

  if request.is_ajax():
        return JsonResponse(params)

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


