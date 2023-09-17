from rest_framework import serializers

from stockdata.models import Data


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'