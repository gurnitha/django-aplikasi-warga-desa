# rw/models.py

from django.db import models

# Create your models here.

class RukunWarga(models.Model):

	rw 		= models.CharField(max_length=50)
	ketua 	= models.CharField(max_length=50)
	alamat 	= models.CharField(max_length=100)
	hp 		= models.CharField(max_length=20)

	class Meta:
		verbose_name = "RW"
		verbose_name_plural = "RW"

	def __str__(self):
		return self.rw
    