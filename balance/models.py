from django.db import models

class Income(models.Model):
  name = models.CharField(('項目名'), max_length=255)
  amount = models.FloatField(('金額'), max_length=255)
  date = models.DateField(('日付'))

  def __str__(self) -> str:
    return self.name

  class Meta:
    verbose_name = ('income')
    verbose_name_plural = ('incomes')

class Expense(models.Model):
  name = models.CharField(('項目名'), max_length=255)
  amount = models.FloatField(('金額'), max_length=255)
  date = models.DateField(('日付'))

  def __str__(self) -> str:
    return self.name

  class Meta:
    verbose_name = ('expense')
    verbose_name_plural = ('expenses')

class Category(models.Model):
  pass

  CHOICES = []
