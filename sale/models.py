from django.db import models

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