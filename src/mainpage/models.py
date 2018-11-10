from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=300)
