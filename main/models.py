from django.db import models

# Create your models here.


class user_data(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    age = models.IntegerField()
    nationality = models.CharField(max_length=250)
