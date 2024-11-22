from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import date
import datetime

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, verbose_name="Foto de Perfil")
    pass

# salas channels-redis

class Sala (models.Model):
    name = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 100, default="proyecto ... ")
    fechai = models.DateField(default=datetime.date.today)
    fechaf = models.DateField(blank=True, null= True)
    user = models.ManyToManyField(User, related_name='room_joined', blank= True) 

    def __str__(self):
        return self.name
    
    def progreso(self):
        total_dias = (self.fechaf - self.fechai).days
        dias_pasados = (date.today() - self.fechai).days
        if total_dias <= 0:
            return 100  # Evitar dividir por cero
        progreso = (dias_pasados / total_dias) * 100
        return min(max(progreso, 0), 100)  

