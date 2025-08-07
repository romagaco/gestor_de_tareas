from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Usuario')
    title = models.CharField(max_length=100, verbose_name='Título')
    caption = models.TextField(max_length=500, blank=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Comment(models.Model):
    task = models.ForeignKey(Task, verbose_name='Task al que pertenece el comentario', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='Contenido del comentario', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created_at']

    def __str__(self):
        return f"Coméntó {self.user.username} el post {self.task}"