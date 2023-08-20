from django.db import models
from django.contrib.auth.models import User

class Subfolder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    class Meta:
        unique_together = ('name','user')
        
    def __str__(self):
        return self.name

class JSONFile(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    subfolder = models.ForeignKey(Subfolder, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
