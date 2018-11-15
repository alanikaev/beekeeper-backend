from django.db import models

class Companies(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=500)
	date = models.DateField()
	rating = models.FloatField()
