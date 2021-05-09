# desa/models.py

from django.db import models

# Create your models here.

class NamaDesa(models.Model):

	nama_desa 	= models.CharField(max_length=50)
	kepala_desa = models.CharField(max_length=50)
	alamat_desa = models.CharField(max_length=100)
	hp_kades 	= models.CharField(max_length=20)

	class Meta:
		verbose_name = "Nama desa"
		verbose_name_plural = "Nama desa"

	def __str__(self):
		return self.nama_desa
    