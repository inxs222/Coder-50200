from django.shortcuts import render
from django.db.models import Sum
from .models import *


def home(request):
    debeFacturas = Facturas.objects.filter(nAbonado='14071', pago='no').count()
    
    totalDeuda = Facturas.objects.filter(nAbonado='14071', pago='no').aggregate(total=Sum('monto'))
    
    minDeuda = Facturas.objects.filter(nAbonado='14071', pago='no').aggregate(total=Sum('monto')*0.70)

    context = {'mostrarDashboard': True, 'abonados': Abonado.objects.all(), 'debeFacturas': debeFacturas, 'totalDeuda': totalDeuda['total'], 'minDeuda': minDeuda['total'],
               } 
    return render(request, "abonados/home.html", context)

def facturas(request):
    context = {'mostrarDashboard': False, 'facturas': Facturas.objects.all()} 
    return render(request, "abonados/facturas.html", context)


def facturasPagas(request):
    context = {'mostrarDashboard': False, 'facturas': Facturas.objects.all()} 
    return render(request, "abonados/facturaspagas.html", context)