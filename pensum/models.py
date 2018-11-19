from django.db import models
from django.contrib import admin

class Materia(models.Model):
    nombre  =   models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre    = models.CharField(max_length=60)
    materias = models.ManyToManyField(Materia, through='Seccion')

    def __str__(self):
        return self.nombre


class Seccion(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    extra = 1

class SeccionInLine(admin.TabularInline):
    model = Seccion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (SeccionInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (SeccionInLine,)
