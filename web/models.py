from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5500)
    published_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'
        ordering = ['published_at']

    def __str__(self):

        return self.title
