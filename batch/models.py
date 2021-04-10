from django.db import models


class Stock(models.Model):

    name = models.CharField(verbose_name='stock name', max_length=255)
    price = models.DecimalField(verbose_name='stock price', max_digits=19, decimal_places=2)
    date = models.DateField(verbose_name='stock price date')

    class Meta:
        db_table = 'stock'
