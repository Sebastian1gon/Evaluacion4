from django.db import models

# Create your models here.

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_Institucion=models.CharField(max_length=255)

    def __str__(self):
        return(self.Nombre_Institucion)

class Inscritos(models.Model):
    idins=models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10,unique=True)
    nombre=models.CharField(max_length=255)
    telefono=models.IntegerField()
    fecha_inscripcion =models.DateField()
    hora_inscripcion = models.TimeField()
    institucion=models.ForeignKey(Institucion,on_delete=models.CASCADE,related_name='inscritos')
    estado=models.CharField(max_length=255)
    observacion=models.CharField(max_length=255)