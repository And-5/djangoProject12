from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    photo = models.ImageField()

class Person_1(models.Model):

    name = models.CharField(
        max_length=100)
    credit_card_number = models.CharField(
        max_length=90,
        db_index=True
    )