from django.contrib.auth.models import User
from django.db import models

from account.models import AdvUser
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
        ('m', 'MALE'),
        ('f', 'FEMALE'),
        ('o', 'OTHER'),)

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

    chipper = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=False)
    chippingLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=False,
                                         related_name='chipping_location')
    animalTypes = models.ManyToManyField(Type)
    chippingDateTime = models.DateTimeField(auto_now=True)
    deathDateTime = models.DateTimeField(null=True, blank=False)
    visitedLocations = models.ManyToManyField(Location, related_name='visited_location')
