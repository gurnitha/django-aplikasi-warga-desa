# warga/admin.py

from django.contrib import admin
from app.warga.models import Warga

# Register your models here.
# admin.site.register(Warga)
@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
	list_display = (
			'nama_lengkap',
			'nik',
			'rw',
			'rt',
			'covid',
			'status_perawatan',
			'penghasilan_per_bulan')

	list_filter = (
			'covid',
			'penghasilan_per_bulan'
			
		)
