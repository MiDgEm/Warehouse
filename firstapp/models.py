from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=15)
    article = models.CharField(max_length=13)
    state = models.CharField(max_length=13)
    price = models.IntegerField()
    description = models.TextField(max_length=1500)
    image = models.BinaryField()
