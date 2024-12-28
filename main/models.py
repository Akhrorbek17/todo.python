from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=550, verbose_name = 'Todo title')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['done']