# rt/models.py

from django.db import models

# Create your models here.

class RukunTetangga(models.Model):

	rt 		= models.CharField(max_length=50)
	ketua 	= models.CharField(max_length=50)
	alamat 	= models.CharField(max_length=100)
	hp 		= models.CharField(max_length=20)

	class Meta:
		verbose_name = "RT"
		verbose_name_plural = "RT"

	def __str__(self):
		return self.rt