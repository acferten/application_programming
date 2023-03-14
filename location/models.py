from django.db import models


class Location(models.Model):
    latitude = models.DecimalField(max_digits=15, decimal_places=13)
    longitude = models.DecimalField(max_digits=15, decimal_places=13)

    def __str__(self):
        return '%s, %s' % (self.latitude, self.longitude)
