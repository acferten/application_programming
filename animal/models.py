from django.contrib.auth.models import User
from django.db import models

from location.models import Location


class Type(models.Model):
    type = models.CharField(max_length=1000)

    def __str__(self):
        return self.type


class Animal(models.Model):
    weight = models.FloatField()
    length = models.FloatField()
    height = models.FloatField()

    GENDER_TYPES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_TYPES,
        null=False,
        help_text='Пол')

    LIFE_STATUS = (
        ('a', 'ALIVE'),
        ('d', 'DEAD'))

    lifeStatus = models.CharField(
        max_length=1,
        choices=LIFE_STATUS,
        default='a',
        null=False,
        help_text='Жизненный статус')

    chipper = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    chippingLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=False,
                                         related_name='chipping_location')
    animalTypes = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    chippingDateTime = models.DateTimeField(auto_now=True)
    deathDateTime = models.DateTimeField(null=True, blank=False)
    visitedLocations = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='visited_location')
