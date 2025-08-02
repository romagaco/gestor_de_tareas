from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField('Biografía', max_length=500, blank=True)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    first_name = models.CharField('Nombre', max_length=30, blank=True)
    last_name = models.CharField('Apellido', max_length=30, blank=True)
    


    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        return self.user.username