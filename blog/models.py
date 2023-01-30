from django.db import models

# Create your models here.

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=150)
    sana = models.DateField()
    matn = models.TextField()
    rasm = models.FileField()

    def __str__(self):
        return self.sarlavha

class Intervyu(models.Model):
    sarlavha = models.CharField(max_length=150)
    sana = models.DateField()
    link = models.CharField(max_length=100)
    rasm = models.FileField()

    def __str__(self):
        return self.sarlavha