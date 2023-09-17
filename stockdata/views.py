# books/views.py
from rest_framework import viewsets

from stockdata.models import Data
from stockdata.serializer import StocksSerializer
from rest_framework.decorators import action
from stockdata.models import search_sql_by_stock
from rest_framework.response import Response
from rest_framework import status
class StocksViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = StocksSerializer

    @action(detail=False,methods=['get'])
    def sql_cursor(self, request):
        stock = request.query_params.get('stock', None)
        number_min = request.query_params.get('number_min', None)
        number_max = request.query_params.get('number_max', None)
        if stock:
            data = search_sql_by_stock(stock,number_min,number_max)
            return Response(data, status=status.HTTP_200_OK)
  