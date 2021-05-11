# warga/models.py

from django.db import models
from app.desa.models import Desa
from app.rw.models import RukunWarga
from app.rt.models import RukunTetangga 

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

	# # PEKERJAAN
	# APARATUR_SIPIL_NEGARA = 'Asn'
	# ANGAKAT_DARAT = 'Ad'
	# ANGKATAN_UDARA = 'Au'
	# ANGKATAN_LAUT = 'Al'
	# WIRA_SWASTA = 'Wswt'
	# PENSIUNAN = 'Pensiun'

	# jenis_pekerjaan_pilihan = [
	# 	(APARATUR_SIPIL_NEGARA, 'PNS'),
	# 	(ANGAKAT_DARAT,'Angkatan Darat'),
	# 	(ANGKATAN_UDARA, 'Angkatan Laut'),
	# 	(ANGKATAN_LAUT, 'Angkatan Laut'),
	# 	(WIRA_SWASTA, 'Wira Swasta'),
	# 	(PENSIUNAN, 'Pensiun'),
	# ]

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
	TIDAK_TERPAPAR 		= 'TIDAK TERPAPAR'
	TERPAPAR_COVID_19 	= 'TERPAPAR COVID-19'
	TERPAPAR_VARIAN_BARU= 'TERPAPAR VARIAN BARU'

	covid_pilihan = [
		(TIDAK_TERPAPAR, 'Tidak'),
		(TERPAPAR_COVID_19, 'Terpapar Covid-19'),
		(TERPAPAR_VARIAN_BARU, 'Terpapar varian baru')
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


	# KONDISI EKONOMI WARGA
	## 1. Profesi
	PEMULUNG 	= 'Pemulung'
	TUKANG 		= 'Tukang'
	OJEK 		= 'Ojek'
	SOPIR 		= 'Sopir'
	PETANI 		= 'Petani'
	PEDAGANG_K5 = 'K5'
	PEDAGANG_WARUNG = 'Pedagang Warung'
	ART 		= 'AST'
	ASN 		= 'ASN'
	AMN 		= 'AMN'
	POLISI 		= 'Polisi'
	GURU 		= 'Guru'
	DOSEN 		= 'Dosen'
	PROFESIONAL = 'Profesional'
	WIRA_SWASTA = 'Wira Swasta'
	PENSIUNAN 	= 'Pensiunan'
	PEGAWAI_HONORER = 'Honorer'
	LAIN_LAIN 	= 'Lain Lain'	
	
	profesi_pilihan = [	
		(PEMULUNG 	, 'Pemulung'),
		(TUKANG 		, 'Tukang'),
		(OJEK 		, 'Ojek'),
		(SOPIR 		, 'Sopir'),
		(PETANI 		, 'Petani'),
		(PEDAGANG_K5 , 'K5'),
		(PEDAGANG_WARUNG , 'Pedagang warung'),
		(ART 		, 'AST'),
		(ASN 		, 'ASN'),
		(AMN 		, 'AMN'),
		(POLISI 		, 'Polisi'),
		(GURU 		, 'Guru'),
		(DOSEN 		, 'Dosen'),
		(PROFESIONAL , 'Profesional'),
		(WIRA_SWASTA , 'Wira Swasta'),
		(PENSIUNAN 	, 'Pensiunan'),
		(PEGAWAI_HONORER , 'Honorer'),
		(LAIN_LAIN 	, 'Lain lain')
	]

	## 2. Penghasilan per bulan 
	KURANG_DARI_SATU_JUTA 			= 'Kurang 1 Juta'
	KURANG_DARI_SATU_SETENGAH_JUTA 	= 'Sampai 1,5 Juta'
	KURANG_DARI_DUA_JUTA 			= 'Kurang dari 2 Juta'
	KURANG_DARI_DUA_SETENGAH_JUTA	= 'Kurang dari 2,5 Juta'
	KURANG_DARI_TIGA_JUTA 			= 'Kurang dari 3 Juta'
	KURANG_DARI_TIGA_SETENGAH_JUTA	= 'Kurang dari 3,5 Juta'
	KURANG_DARI_EMPAT_JUTA 			= 'Kurang dari 4 Juta'
	KURANG_DARI_LIMA_JUTA 			= 'Kurang dari 5 Juta'
	KURANG_DARI_TUJUH_JUTA 			= 'Kurang dri 7 Juta'
	KURAND_DARI_SEPULUH_JUTA 		= 'Kurang dari 10 Juta'
	LEBIH_DARI_SEPULUH_JUTA 		= 'Lebih dari 10 Juta'

	penghasilan_per_bulan_pilihan = [
		(KURANG_DARI_SATU_JUTA 			, 'Kurang 1 juta'),
		(KURANG_DARI_SATU_SETENGAH_JUTA 	, 'Sampai 1,5 juta'),
		(KURANG_DARI_DUA_JUTA 			, 'Kurang dari 2 juta'),
		(KURANG_DARI_DUA_SETENGAH_JUTA	, 'Kurang dari 2,5 juta'),
		(KURANG_DARI_TIGA_JUTA 			, 'Kurang dari 3 juta'),
		(KURANG_DARI_TIGA_SETENGAH_JUTA	, 'Kurang dari 3,5 juta'),
		(KURANG_DARI_EMPAT_JUTA 			, 'Kurang dari 4 juta'),
		(KURANG_DARI_LIMA_JUTA 			, 'Kurang dari 5 juta'),
		(KURANG_DARI_TUJUH_JUTA 			, 'Kurang dri 7 juta'),
		(KURAND_DARI_SEPULUH_JUTA 		, 'Kurang dari 10 juta'),
		(LEBIH_DARI_SEPULUH_JUTA 		, 'Lebih dari 10 juta')
	]	

	## 3. Jumlah anggota keluarga
	SATU_ORANG 		= '1 Orang'
	DUA_ORANG 		= '2 Orang'
	TIGA_ORANG 		= '3 Orang'
	EMPAT_ORANG 	= '4 Orang'
	LIMA_ORANG 		= '5 Orang'
	ENAM_ORANG 		= '6 Orang'
	TUJUH_ORANG 	= '7 Orang'
	DELAPAN_ORANG 	= '8 Orang'
	SEMBILAN_ORANG 	= '9 Orang'
	SEPULUH_ORANG 	= '10 Orang'
	LEBIH_DARI_SEPULUH_ORANG = 'Lebih Dari 10 Orang'

	jumlah_angota_keluarga_pilihan = [
		(SATU_ORANG 		, '1 orang'),
		(DUA_ORANG 		, '2 orang'),
		(TIGA_ORANG 		, '3 orang'),
		(EMPAT_ORANG 	, '4 orang'),
		(LIMA_ORANG 		, '5 orang'),
		(ENAM_ORANG 		, '6 orang'),
		(TUJUH_ORANG 	, '7 orang'),
		(DELAPAN_ORANG 	, '8 orang'),
		(SEMBILAN_ORANG 	, '9 orang'),
		(SEPULUH_ORANG 	, '10 orang'),
		(LEBIH_DARI_SEPULUH_ORANG , 'Lebih Dari 10 orang')
	]	

	## 4. Jenis rumah tempat tinggal
	PETAKAN_LANTAI_TANAH 	= 'Petakan Lantai Tanah'
	PETAKAN_LANTAI_SEMEN	= 'Petakan Lantai Semen'
	PETAKAN_LANTAI_KERAMIK 	= 'Petakan Lantai Keramik'
	RUMAH_SEMI_PERMANEN 	= 'Rumah Semi Permanen'
	RUMAH_PERMANEN 			= 'Rumah Permanen' 

	jenis_rumah_tempat_tingal_pilihan = [
		(PETAKAN_LANTAI_TANAH 	, 'Petakan Lantai Tanah'),
		(PETAKAN_LANTAI_SEMEN	, 'Petakan Lantai Semen'),
		(PETAKAN_LANTAI_KERAMIK 	, 'Petakan Lantai Keramik'),
		(RUMAH_SEMI_PERMANEN 	, 'Rumah Semi Permanen'),
		(RUMAH_PERMANEN 			, 'Rumah Permanen') 
	]


	## 5. Status rumah tempat tinggal
	SEWA 			= 'Sewa'
	MILIK_ORANG_TUA = 'Milik Orang Tua'
	MILIK_SENDIRI 	= 'Milik Sendiri'

	status_rumah_tempat_tinggal_pilihan = [
		(SEWA 			, 'Sewa'),
		(MILIK_ORANG_TUA , 'Milik Orang Tua'),
		(MILIK_SENDIRI 	, 'Milik Sendiri')
	]		




	"""---------------KOLOM TABEL---------------------"""

	"""IDENTITAS UTAMA WARGA"""
	nama_lengkap   	= models.CharField(
						max_length=100,
						help_text='Boleh dikosongkan.')
	nama_panggilan 	= models.CharField(
						max_length=30,
						help_text='Boleh dikosongkan.')
	nik            	= models.CharField(
						max_length=20,
						help_text='Boleh dikosongkan.')
	hp            	= models.CharField(
						max_length=20, 
						null=True,
						help_text='Boleh dikosongkan.')

	
	"""KEWARGAAN DESA/RW/RT"""
	desa = models.ForeignKey(
						Desa, 
						on_delete=models.CASCADE,
						help_text='Klik tanda panah.')
	rw = models.ForeignKey(
						RukunWarga, 
						on_delete=models.CASCADE,
						help_text='Klik tanda panah.')
	rt = models.ForeignKey(
						RukunTetangga, 
						on_delete=models.CASCADE,
						help_text='Klik tanda panah.')
    	
	
	"""IDENTITAS TAMBAHAN WARGA"""
	jenis_kelamin  	= models.CharField(
						max_length=10,
						choices=gender_pilihan,
						help_text='Klik tanda panah.')
	tempat_lahir   	= models.CharField(
						max_length=50, 
						null=True,
						help_text='Contoh: Denpasar, Bali atau Boleh dikosongkan.')
	tanggal_lahir   = models.CharField(
						max_length=12, 
						null=True,
						help_text='Contoh: 01/01/2001 atau Boleh dikosongkan.')
	agama          	= models.CharField(
						max_length=10,
						choices=agama_pilihan,
						help_text='Klik tanda panah.')
	pend_tertinggi 	= models.CharField(
						max_length=10,
						choices=pendidikan_pilihan,
						help_text='Klik tanda panah.')
	# jenis_pekerjaan = models.CharField(
	# 					max_length=20,
	# 					choices=jenis_pekerjaan_pilihan,
	# 					help_text='Klik tanda panah.')
	status_perkawinan 	= models.CharField(
						max_length=10,
						choices=status_perkawinan_pilihan,
						help_text='Klik tanda panah.')
	status_hub_dlm_kel 	= models.CharField(
						max_length=30,
						choices=status_hub_dlm_kel_pilihan,
						help_text='Klik tanda panah.')
	nama_ibu 		= models.CharField(
						max_length=50, 
						null=True,
						help_text='Boleh dikosongkan.')
	nama_ayah 		= models.CharField(
						max_length=50, 
						null=True,
						help_text='Boleh dikosongkan.')


	"""TEMPAT TINGGAL WARGA"""
	alamat_tempat_tinggal 	= models.CharField(
								max_length=100, 
								help_text='Tidak boleh dikosongkan.')

	"""KESEHATAN UMUM"""
	kondisi_kesehatan 	= models.CharField(
							max_length=30,
							choices=kondisi_kesehatan_pilihan, 
							help_text='Klik tanda panah.')
	penyakit_khusus 	= models.CharField(
							max_length=30,
							choices=penyakit_khusus_pilihan, 
							help_text='Klik tanda panah.')


	# KESEHATAN KHUSUS COVID
	covid 	 			= models.CharField(
							max_length=30,
							choices=covid_pilihan,
							help_text='Klik tanda panah.')
	waktu_terpapar 		= models.CharField(
							max_length=30,
							help_text='Contoh: 01/05/2021')
	gejala_saat_terpapar= models.TextField(
							null=True,
							help_text='Boleh dikosongkan.')
	status = models.CharField(
							max_length=30,
							choices=kondisi_kesehatan_setelah_terpapar_pilihan,
							help_text='Klik tanda panah.')


	# KONDISI EKONOMI WARGA
	""" 1. Profesi (
			PEMULUNG, TUKANG, OJEK, SOPIR, PETANI, PEDAGANG K5, PEDAGANG TETAP,
			ART, ASN, AMN, POLISI, GURU, DOSEN, PROFESIONAL, WIRA SWASTA,
			PENSIUNAN, LAIN-LAIN ) """
	profesi 			= models.CharField(
							max_length=30,
							choices=profesi_pilihan,
							help_text='Klik tanda panah.')	

	""" 2. Penghasilan per bulan (
			Rp kurang dari 1 juta, 
			Rp 1-1,5 juta, 
			Rp kurang dari 2 juta,
			Rp kurang dari 2,5 juta
			Rp kurang dari 3 juta
			Rp kurang dari 3,5 juta
			Rp kurang dari 4 juta
			Rp lebih dari 4 juta"""
	penghasilan_per_bulan 	= models.CharField(
							max_length=30,
							choices=penghasilan_per_bulan_pilihan,
							help_text='Klik tanda panah.')	

	""" 3. Jumlah anggota keluarga(
			1 orang, 2 orang, 3 orang, 4 orang, 5 orang,
			6 orang, 7 orang, 8 orang, 9 orang, 10 orang,
			lebih dari 10 orang) """
	jumlah_anggota_keluarga = models.CharField(
							max_length=30,
							choices=jumlah_angota_keluarga_pilihan,
							help_text='Klik tanda panah.')	
	
	""" 4. Jenis rumah tempat tinggal (
			petakan lantai tanah,
			petakan lantai semen,
			petakan lantai keramik,
			semi permanen,
			permanen)"""
	jenis_rumah_tempat_tingal = models.CharField(
							max_length=30,
							choices=jenis_rumah_tempat_tingal_pilihan,
							help_text='Klik tanda panah.')	
	
	""" 5. Status rumah tempat tinggal (
			sewa, milik orang tua, milik sendiri)"""
	status_rumah_tempat_tinggal = models.CharField(
							max_length=30,
							choices=status_rumah_tempat_tinggal_pilihan,
							help_text='Klik tanda panah.')	
	class Meta:
		verbose_name = "Warga"
		verbose_name_plural = "Warga"

	def __str__(self):
		return self.nama_lengkap




    


