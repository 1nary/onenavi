from django.contrib import admin
from .models import SaleItem, SaleFavorite

class SaleItemAdmin(admin.ModelAdmin):
    list_display=('id','name','price','date','shop')

admin.site.register(SaleItem,SaleItemAdmin)
admin.site.register(SaleFavorite)