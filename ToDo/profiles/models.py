from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField('Imagen de perfil', upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField('Biografía', max_length=500, blank=True)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    first_name = models.CharField('Nombre', max_length=30, blank=True)
    last_name = models.CharField('Apellido', max_length=30, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username