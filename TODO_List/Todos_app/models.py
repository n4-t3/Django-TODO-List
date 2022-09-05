from django.db import models
from Authentication_App.models import Person
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    tasks = models.CharField(max_length=200)

    def __str__(self):
        return self.tasks
