# Generated by Django 3.2 on 2021-05-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warga',
            name='kewarganegaraan',
        ),
        migrations.AddField(
            model_name='warga',
            name='tanggal_lahir',
            field=models.CharField(help_text='Contoh: 01/01/2001', max_length=50, null=True),
        ),
    ]
