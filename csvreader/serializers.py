from rest_framework import serializers
from .models import CSVdata


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVdata
        fields = '__all__'

