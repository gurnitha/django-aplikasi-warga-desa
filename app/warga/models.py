# warga/models.py

from django.db import models
from app.desa.models import NamaDesa
from app.rt.models import NamaRt
from app.rw.models import NamaRw 

class Warga(models.Model):

	# AGAMA
	ISLAM 	= 'Isl'
	KRISTEN = 'Kris'
	KATOLIK = 'Kat'
	HINDU   = 'Hin'
	KONGHUCU= 'Kong'

	agama_pilihan = [
		(ISLAM, 'Islam'),
		(KRISTEN, 'Kristen'),
		(KATOLIK, 'Katolik'),
		(HINDU, 'Hindu'),
		(KONGHUCU, 'Konghucu'),
	]

	# JENIS KELAMIT
	LAKI_LAKI = 'L'
	PEREMPUAN = 'P'

	gender_pilihan = [
		(LAKI_LAKI, 'Laki'),
		(PEREMPUAN, 'Perem')
	]

	# PENDIDIKAN
	TIDAK_DIKETAHUI = '-'
	SD 	= 'SD'
	SMP = 'SMP/SETARA'
	SMU = 'SMU/SETARA'
	SMK = 'SMK'
	SARAJANA = 'S1'
	MASTER 	 = 'S2'
	DOKTOR   = 'DR'
	PROFESOR = 'PROP'

	pendidikan_pilihan = [
		(TIDAK_DIKETAHUI, 'Tidak diketahui'),
		(SD, 'SD'),
		(SMP, 'SMP/SETARA'),
		(SMU, 'SMU/SETARA'),
		(SMK, 'SMK'),
		(SARAJANA, 'S1'),
		(MASTER, 'S2'),
		(DOKTOR, 'DR'),
		(PROFESOR, 'Prof')
	]

	# PEKERJAAN
	APARATUR_SIPIL_NEGARA = 'Asn'
	ANGAKAT_DARAT = 'Ad'
	ANGKATAN_UDARA = 'Au'
	ANGKATAN_LAUT = 'Al'
	WIRA_SWASTA = 'Wswt'
	PENSIUNAN = 'Pensiun'

	jenis_pekerjaan_pilihan = [
		(APARATUR_SIPIL_NEGARA, 'PNS'),
		(ANGAKAT_DARAT,'Angkatan Darat'),
		(ANGKATAN_UDARA, 'Angkatan Laut'),
		(ANGKATAN_LAUT, 'Angkatan Laut'),
		(WIRA_SWASTA, 'Wira Swasta'),
		(PENSIUNAN, 'Pensiun'),
	]

	# STATUS PERKAWINAN
	BELUM_MENIKAH = 'BM'
	SUDAH_MENIKAH = 'SM'
	JANDA 		  = 'JD'
	DUDA 		  = 'DD'

	status_perkawinan_pilihan = [
		(BELUM_MENIKAH, 'Belum menikah'),
		(SUDAH_MENIKAH, 'Menikah'),
		(JANDA, 'Janda'),
		(DUDA,'Duda')
	]

	# STATUS HUB DALAM KELUARGA
	KEPALA_KELUARGA = 'KK'
	SUAMI 			= 'SU'
	ISTRI 			= 'IS'
	ANAK_KANDUNG 	= 'AK'
	ANAK_ANGKAT 	= 'AA'
	ANAK_TIRI		= 'AI'

	status_hub_dlm_kel_pilihan = [
		(KEPALA_KELUARGA, 'Kepala Keluarga'),
		(SUAMI, 'Suami'),
		(ISTRI, 'Istri'),
		(ANAK_KANDUNG, 'Anak Kandung'),
		(ANAK_ANGKAT, 'Anak Angkat'),
		(ANAK_TIRI, 'Anak Tiri')
	]


	# STATUS TEMPAT TINGGAL
	RUMAH_SENDIRI = 'MILIK'
	RUMAH_ORANG_TUA = 'ORTU'
	MENGONTRAK 	  = 'SEWA'

	status_tempat_tinggal_pilihan = [
		(RUMAH_SENDIRI, 'Rumah sendiri'),
		(RUMAH_ORANG_TUA, 'Rumah orang tua'),
		(MENGONTRAK, 'Sewa')
	]

	# STATUS KESEHATAN
	## Kondisi Kesehatan Umum 
	BAIK 		= 'B'
	KURANG_BAIK = 'KB'

	kondisi_kesehatan_pilihan = [
		(BAIK, 'Baik'),
		(KURANG_BAIK, 'Kurang baik')
	]

	## Penyakit khusus
	JANTUNG 	= 'JTG'
	DIABITES 	= 'DIABET'
	ASMA 		= 'ASMA'
	PARU_PARU 	= 'PARU'
	HIV_AIDS 	= 'HIV'
	GINJAL 		= 'GJAL'
	TIDAK_ADA 	= 'TA'

	penyakit_khusus_pilihan = [
		(JANTUNG, 'Jantung'),
		(DIABITES, 'Diabet'),
		(ASMA, 'Asma'),
		(PARU_PARU, 'Paru'),
		(HIV_AIDS, 'Hiv'),
		(GINJAL, 'Ginjal'),
		(TIDAK_ADA, 'Tidak ada')
	]

	# COVID
	TIDAK_TERPAPAR_COVID_19 = 'TIDAK TERPAPAR'
	TERPAPAR_COVID_19 	= 'TERPAPAR'

	covid_19_pilihan = [
		(TIDAK_TERPAPAR_COVID_19, 'Tidak'),
		(TERPAPAR_COVID_19, 'Terpapar')
	]

	# KONDISI STLH TERPAPAR COVID
	ISOLASI_MANADIRI = 'ISOLASI'
	DIRAWAT_DI_RS	 = 'DIRAWAT'
	PULIH_NORMAL	 = 'PULIH'
	TIDAK_TERPAPAR 	 = 'TDK TERPAPAR'

	kondisi_kesehatan_setelah_terpapar_pilihan = [
		(ISOLASI_MANADIRI, 'Isolasi mandiri'),
		(DIRAWAT_DI_RS, 'Dirawat di RS'),
		(PULIH_NORMAL, 'Pulih normal'),
		(TIDAK_TERPAPAR, '-')
	]

	"""IDENTITAS WARGA"""
	nama_lengkap   	= models.CharField(max_length=100)
	nama_panggilan 	= models.CharField(max_length=30)
	nik            	= models.CharField(max_length=20)
	
	"""WARGA DESA/RW/RT"""
	desa = models.ForeignKey(
						NamaDesa, on_delete=models.CASCADE,
						help_text='Klik tanda panah')
	rw = models.ForeignKey(
						NamaRw, on_delete=models.CASCADE,
						help_text='Klik tanda panah')
	rt = models.ForeignKey(
						NamaRt, on_delete=models.CASCADE,
						help_text='Klik tanda panah')
    	
	jenis_kelamin  	= models.CharField(
						max_length=10,
						choices=gender_pilihan,
						help_text='Klik tanda panah')
	tempat_lahir   	= models.CharField(max_length=50, null=True)
	tanggal_lahir   = models.CharField(
						max_length=12, 
						help_text="Contoh: 01/01/2001", null=True)
	agama          	= models.CharField(
						max_length=10,
						choices=agama_pilihan,
						help_text='Klik tanda panah')
	pend_tertinggi 	= models.CharField(
						max_length=10,
						choices=pendidikan_pilihan,
						help_text='Klik tanda panah')
	jenis_pekerjaan = models.CharField(
						max_length=20,
						choices=jenis_pekerjaan_pilihan,
						help_text='Klik tanda panah')
	status_perkawinan 	= models.CharField(
						max_length=10,
						choices=status_perkawinan_pilihan,
						help_text='Klik tanda panah')
	status_hub_dlm_kel 	= models.CharField(
						max_length=30,
						choices=status_hub_dlm_kel_pilihan,
						help_text='Klik tanda panah')
	nama_ibu 		= models.CharField(max_length=50, null=True)
	nama_ayah 		= models.CharField(max_length=50, null=True)


	"""TEMPAT TINGGAL"""
	tempat_tinggal 	= models.CharField(max_length=100, null=True)
	status_tempat_tinggal 	= models.CharField(
						max_length=30,
						choices=status_tempat_tinggal_pilihan, 
						null=True,
						help_text='Klik tanda panah')

	"""KESEHATAN"""
	# kondisi_kesehatan 	= models.ManyToManyField(KesehatanWarga)
	kondisi_kesehatan 	= models.CharField(
							max_length=30,
							choices=kondisi_kesehatan_pilihan, 
							null=True,
							help_text='Klik tanda panah')
	penyakit_khusus 	= models.CharField(
							max_length=30,
							choices=penyakit_khusus_pilihan, 
							null=True,
							help_text='Klik tanda panah')

	covid_19 			= models.CharField(
							max_length=30,
							choices=covid_19_pilihan,
							null=True,
							help_text='Klik tanda panah')
	waktu_terpapar 		= models.CharField(
							max_length=30,
							null=True,
							help_text='Contoh: 01/05/2021')
	gejala_saat_terpapar= models.TextField(null=True)

	status = models.CharField(
							max_length=30,
							null=True,
							choices=kondisi_kesehatan_setelah_terpapar_pilihan,
							help_text='Klik tanda panah')

	class Meta:
		verbose_name = "Warga"
		verbose_name_plural = "Warga"

	def __str__(self):
		return self.nama_lengkap




    


