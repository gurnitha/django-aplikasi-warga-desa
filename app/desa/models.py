# desa/models.py

from django.db import models

# Create your models here.

class Desa(models.Model):

	desa 	= models.CharField(max_length=50)
	kepala 	= models.CharField(max_length=50)
	alamat 	= models.CharField(max_length=100)
	hp 		= models.CharField(max_length=20)

	class Meta:
		verbose_name = "Desa"
		verbose_name_plural = "Desa"

	def __str__(self):
		return self.desa
    