# rw/models.py

from django.db import models

# Create your models here.

class NamaRw(models.Model):

	nama_rw 		= models.CharField(max_length=50)
	nama_ketua_rw 	= models.CharField(max_length=50)
	alamat_rw 		= models.CharField(max_length=100)
	hp_ketua_rw 	= models.CharField(max_length=20)

	class Meta:
		verbose_name = "Nama rw"
		verbose_name_plural = "Nama rw"

	def __str__(self):
		return self.nama_rw
    