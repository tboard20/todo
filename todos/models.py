from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    deccription = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    Created_at =models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.title