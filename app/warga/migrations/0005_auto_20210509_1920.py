# Generated by Django 3.2 on 2021-05-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warga', '0004_auto_20210509_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warga',
            old_name='kondisi_kesehatan_saat_ini',
            new_name='kondkes_saat_ini',
        ),
        migrations.AlterField(
            model_name='warga',
            name='covid_19',
            field=models.CharField(choices=[('TIDAK TERPAPAR', 'Tdk terpapar'), ('TERPAPAR', 'Terpapar')], help_text='Klik tanda panah', max_length=30, null=True),
        ),
    ]
