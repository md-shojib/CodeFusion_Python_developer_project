from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=10)
    capital = models.CharField(max_length=255, blank=True, null=True)
    population = models.BigIntegerField()
    region = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
    flag = models.URLField()
    languages = models.JSONField()

    def __str__(self):
        return self.name
