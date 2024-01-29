from django.db import models

# Create your models here.
class Abonado(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    nAbonado = models.IntegerField()

class Facturas(models.Model):
    nAbonado = models.IntegerField()
    nFactura = models.IntegerField()
    monto = models.IntegerField()
    date = models.IntegerField()
    servicio = models.IntegerField()
    pago = models.CharField(max_length=2)