from django.db import models

class Orders(models.Model):
    order = models.CharField(max_length=150)
    quantity = models.IntegerField()
    cost = models.FloatField()

