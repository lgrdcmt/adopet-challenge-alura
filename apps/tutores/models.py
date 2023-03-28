from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=70, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=11, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    sobre = models.TextField(max_length=255, blank=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.nome