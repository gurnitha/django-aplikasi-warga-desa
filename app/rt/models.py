# rt/models.py

from django.db import models

# Create your models here.

class NamaRt(models.Model):

	nama_rt 		= models.CharField(max_length=50)
	nama_ketua_rt 	= models.CharField(max_length=50)
	alamat_rt 		= models.CharField(max_length=100, null=True)
	hp_ketua_rt 	= models.CharField(max_length=20, null=True)

	class Meta:
		verbose_name = "Nama rt"
		verbose_name_plural = "Nama rt"

	def __str__(self):
		return self.nama_rt