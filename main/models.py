from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.TextField()
    name = models.CharField(max_length=250, blank=True, default="Anonymous")
    institute = models.CharField(max_length=250, blank=True,
                                 default="Anonymous")
