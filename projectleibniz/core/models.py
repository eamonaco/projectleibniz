from django.db import models

class Prova(models.Model):
    titulo = models.CharField(max_length=255)
    periodo = models.CharField(max_length=10)
    arquivo = models.FileField(upload_to="")
    