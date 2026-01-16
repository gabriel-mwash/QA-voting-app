from django.db import models

# Create your models here.


class user_data(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    age = models.IntegerField()
    nationality = models.CharField(max_length=250)


class User(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)


class Question(models.Model):
    question = models.TextField()
    name = models.CharField(max_length=250, blank=True, default="Anonymous")
    institute = models.CharField(max_length=250, blank=True, default="Anonymous")
