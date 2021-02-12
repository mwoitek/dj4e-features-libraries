from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=8)


    def __str__(self):
        return self.name


class Iso(models.Model):

    name = models.CharField(max_length=2)


    def __str__(self):
        return self.name


class Region(models.Model):

    name = models.CharField(max_length=31)


    def __str__(self):
        return self.name


class States(models.Model):

    name = models.CharField(max_length=52)


    def __str__(self):
        return self.name


class Site(models.Model):

    name = models.CharField(max_length=130)
    description = models.CharField(max_length=1704, null=True)
    justification = models.CharField(max_length=3604, null=True)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
