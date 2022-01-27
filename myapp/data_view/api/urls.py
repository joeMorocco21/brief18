from django.contrib import admin
from django.urls import path, include
from .views import (
    DataView,
    DataMeans,
    DataStd,
)

urlpatterns = [
    path('', DataView.as_view()),
    path('means/', DataMeans.as_view()),
    path('std/', DataStd.as_view()),
]