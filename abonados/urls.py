from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('facturas/', facturas, name="facturas"),
    path('facturaspagas/', facturasPagas, name="facturasPagas"),
]