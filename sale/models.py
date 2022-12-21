from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class SaleItem(models.Model):
  id = models.IntegerField(('商品ID'), primary_key=True)
  name = models.CharField(('商品名'), max_length=255)
  price = models.FloatField(('税込価格'), max_length=255)
  url = models.CharField(('url'), max_length=255)
  date = models.DateField(('取得日'))
  shop = models.CharField(('店舗名'), max_length=255)

  def __str__(self) -> str:
    return self.name

  class Meta:
    verbose_name = ('item')
    verbose_name_plural = ('items')

class SaleFavorite(models.Model):
  saleitem = models.ForeignKey(SaleItem, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(default=timezone.now)

  def __str__(self) -> str:
    return str(self.saleitem)

  class Meta:
    verbose_name = ('favorite')
    verbose_name_plural = ('favorites')