from django.db import models
from django.urls import reverse ##Genera urls
# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Libro", max_length=200)
    autor = models.CharField(verbose_name="Autor", max_length=200)
    paginas = models.IntegerField(verbose_name="Páginas", default=1)

    class Meta:
        # Ordenar por nombre
        ordering = ['nombre']

    def __str__(self):
        # Muestra el campo nombre
        return self.nombre

class Stock(models.Model):
    libro = models.OneToOneField(Libros, on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name="Cantidad de libros", default=0)

    def __str__(self):
        #### THE NAME IS GOING TO BE DISPLAYED IN THE ADMIN PANNEL ########
        return '{0}'.format(self.stock)
    def get_absolute_url(self):
        return reverse('stock-detail', args=[str(self.id)])

class Biblioteca(models.Model):
    nombre = models.CharField(verbose_name="Nombre de la biblioteca", max_length=200)
    direccion = models.CharField(verbose_name="Dirección", max_length=200)

    def __str__(self):
        return self.nombre
