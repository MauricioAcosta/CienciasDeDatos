from django.db import models

# Create your models here.

class Usuarios (models.Model):
    id = models.AutoField(primary_key='True')
    arroba = models.CharField(max_length=50)
    nombre_cuenta = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cuenta

class Candidatos (models.Model):
    id = models.AutoField(primary_key='True')
    arroba = models.CharField(max_length=50)
    nombre_cuenta = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cuenta


class Hashtags (models.Model):
    id = models.AutoField(primary_key='True')
    hashtag = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag