import csv
import os

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CSVdata
from .serializers import ResultSerializer

from .readfunc import csvsumm, set_file_dir


class StartCalc(APIView):
    serializer_class = ResultSerializer

    def post(self, request):
        file_data = self.request.data
        file_required = set_file_dir(file_data["filename"])
        file_dataresult = csvsumm(file_required, 9)

        serializer = ResultSerializer(data={'filename': file_data["filename"], 'dataresult': file_dataresult})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountInWork(APIView):
    pass


class GetResult(APIView):

    def get(self, request, *args, **kwargs):
        filename = '.'.join([self.request.query_params.get('filename'), 'csv'])
        required_info = CSVdata.objects.get(filename=filename)
        serializer = ResultSerializer(required_info)
        return Response(serializer.data)
