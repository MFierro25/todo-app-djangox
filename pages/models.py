from django.db import models
from django.urls import reverse

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    date_created = models.DateField()
    
    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})