from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class StockBase(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        abstract = True


class Currency(StockBase):

    def __str__(self):
        return f'{self.code}'

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Item(StockBase):
    currency = models.ForeignKey(Currency, blank=False, null=False, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True, max_length=250)

    def __str__(self):
        return f'{self.name} ({self.code})'
