from django.db import models

# Create your models here.

class Voter(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name



