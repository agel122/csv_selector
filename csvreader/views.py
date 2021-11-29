from rest_framework import generics
from rest_framework.views import APIView
from .models import CSVdata
from .serializers import ResultSerializer


class StartCalc(APIView):
    pass


class CountInWork(APIView):
    pass


class GetResult(APIView):
    pass



