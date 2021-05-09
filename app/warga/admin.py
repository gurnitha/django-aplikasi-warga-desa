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
			'rt',
			'rw',
			'covid_19',
			'waktu_terpapar',
			'status')

	list_filter = (
			'status',
			'covid_19',
			'rt'
		)
