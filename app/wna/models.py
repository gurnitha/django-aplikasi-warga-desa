from django.db import models
from app.desa.models import NamaDesa
from app.rt.models import NamaRt
from app.rw.models import NamaRw 
# from django_countries.fields import CountryField

# Create your models here.

class WNA(models.Model):

	# STATUS KEWARGANEGARAAN
	# WARGA_NEGARA_INDONESIA 	= 'WNI'
	# WARGA_NEAGARA_ASING 	= 'WNA'

	# kewarganegaraan_pilihan = [
	# 	(WARGA_NEGARA_INDONESIA, 'WNI'),
	# 	(WARGA_NEAGARA_ASING, 'WNA')
	# ]

	# STATUS DI INDONESIA
	TURIS 	= 'TURIS'
	BEKERJA	= 'BEKERJA'
	MENIKAH = 'MENIKAH'
	MENGUNJUNGI_KELUARGA = 'KUN KELUARGA'

	status_keberadaanya_di_indonesia_pilihan = [
		(TURIS, 'Turis'),
		(BEKERJA, 'Bekerja'),
		(MENIKAH, 'Menikah'),
		(MENGUNJUNGI_KELUARGA, 'Kun keluarga')
	]

	# kewarganegaraan = models.CharField(
	# 		max_length=10,
	# 		choices=kewarganegaraan_pilihan)
	nama = models.CharField(max_length=50)
	nama_negara_asal = models.CharField(
				max_length=30,
				help_text= "Contoh: Amerika Serikat")
	# nama_negara_asal = CountryField(blank_label='(pilih negara)')
	identitas_diri = models.CharField(max_length=10)
	nomor_paspor = models.CharField(max_length=20)
	masa_berlaku = models.CharField(
					max_length=30, 
					help_text="Contoh: 01/01/2016 - 01/01/2021")
	status_keberadaanya_di_indonesia = models.CharField(
				max_length=30,
				choices=status_keberadaanya_di_indonesia_pilihan) 
	dokumen_lainnya = models.CharField(max_length=100, null=True)
	
	"""ALAMAT TINGGAL WNA"""
	alamat_tinggal  = models.CharField(max_length=100)
	desa = models.ForeignKey(
						NamaDesa, on_delete=models.CASCADE,
						help_text='Klik tanda panah')
	rw = models.ForeignKey(
						NamaRw, on_delete=models.CASCADE,
						help_text='Klik tanda panah')
	rt = models.ForeignKey(
						NamaRt, on_delete=models.CASCADE,
						help_text='Klik tanda panah')
	catatan = models.TextField(blank=True)

	class Meta:
		verbose_name = "WNA"
		verbose_name_plural = "WNA"

	def __str__(self):
		return self.nama_negara_asal



