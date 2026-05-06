from django.db import models


# Create your models here.
class Noticia(models.Model):
#class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    texto_noticia = models.TextField()
    fecha = models.DateTimeField('Fecha de publicacion')
    imagen = models.ImageField(upload_to= 'noticias/', null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo
