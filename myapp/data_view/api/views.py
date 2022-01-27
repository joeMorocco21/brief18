from django.shortcuts import render
import sqlite3
from sqlite3 import Error
# Create your views here.
from django.shortcuts import render
from django.template import loader
from ..models import data_view
from .serializers import DataSerializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import json
import pandas as pd

# Create your views here.
class DataView(APIView):
    def get(self, request, *args, **kwargs):
        datas = data_view.objects.all()
        serializer = DataSerializers(datas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DataMeans(APIView):
    def get(self, request, *args, **kwargs):
        con = str(data_view.objects.all().query)
        df = pd.read_sql_query(con, connection)
        s = df.groupby('ville')['prix_m2_ttc'].mean()
        mean_records = s.reset_index().to_json(orient ='records')
        mean = []
        mean = json.loads(mean_records)
        return Response(mean, status=status.HTTP_200_OK)
class DataStd(APIView):
    def get(self, request, *args, **kwargs):
        con = str(data_view.objects.all().query)
        df = pd.read_sql_query(con, connection)
        st = df.groupby('ville')['prix_m2_ttc'].std()
        std_records = st.reset_index().to_json(orient ='records')
        std = []
        std = json.loads(std_records)
        return Response(std, status=status.HTTP_200_OK)

