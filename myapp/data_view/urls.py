from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.DataViews.index),
    path('api/', include('data_view.api.urls')),
    path('apiauth/', include('data_view.apiauth.urls')),
    path('std/', views.std),
]