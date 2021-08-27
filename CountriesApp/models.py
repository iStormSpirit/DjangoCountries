from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)