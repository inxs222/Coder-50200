from django.db import models

# Create your models here.
class Abonado(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    nAbonado = models.IntegerField()

    def __str__(self):
        return f"{self.nAbonado}, {self.apellido.upper()}, {self.nombre.upper()}"

class Facturas(models.Model):
    nAbonado = models.IntegerField()
    nFactura = models.IntegerField()
    monto = models.IntegerField()
    date = models.IntegerField()
    servicio = models.IntegerField()
    pago = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nAbonado}, {self.apellido.upper()}, {self.nFactura}, {self.monto} , {self.date}"

class Alertas(models.Model):
    status = models.BooleanField()
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.status}, {self.mensaje}"