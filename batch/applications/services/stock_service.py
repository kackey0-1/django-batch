import datetime
from decimal import Decimal
# from requests.sessions import Session
from django.db import transaction
from batch.applications.services.app_logic_base import AppLogicBaseService
from batch.models import Stock


class StockService(AppLogicBaseService):

    def __init__(self):
        super().__init__()

    @transaction.atomic()
    def create_stock(self):
        req = {'name': 'test1', 'price': Decimal(123.12), 'date': '2020-10-01'}
        stock = Stock(req)
        stock.save()


if __name__ == '__main__':
    # https://blog.codecamp.jp/programming-python-stockprice
    today = datetime.date.today()
    month_start = today.strftime('%Y-%m-01')
    month_end = today.strftime('%Y-%m-{}').format(str(calendar.monthrange(today.year, today.month)[1]))
    print(month_start)
    print(month_end)
    print(response)
