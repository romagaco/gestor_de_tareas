from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
        title = models.CharField(max_length=200)
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Usuario')
        caption = models.TextField(max_length=500, blank=True, verbose_name='Descripción')
        created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
        completed = models.BooleanField(default=False)

        class Meta:
            verbose_name = 'Task'
            verbose_name_plural = 'Tasks'

        def __str__(self):
            return f"{self.user.username} - {self.created_at}"


class Comment(models.Model):
    post = models.ForeignKey(Task, verbose_name='Post al que pertenece el comentario', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='Contenido del comentario', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created_at']

def __str__(self):
        return f"Comentó {self.user.username} el post {self.post.title} el {self.created_at}"