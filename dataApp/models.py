from django.db import models

class Subfolder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JSONFile(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    subfolder = models.ForeignKey(Subfolder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
