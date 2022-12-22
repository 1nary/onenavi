from django.urls import path
from sale import views

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='sale_top'),
    path('sale/search/', views.SaleSearchView.as_view(), name='sale_search'),
    path('sale/favorite/', views.SaleFavoriteView, name='sale_favorite'),
]
