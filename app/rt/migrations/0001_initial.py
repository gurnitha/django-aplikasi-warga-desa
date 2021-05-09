# Generated by Django 3.2 on 2021-05-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NamaRt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_rt', models.CharField(max_length=50)),
                ('nama_ketua_rt', models.CharField(max_length=50)),
                ('alamat_rt', models.CharField(max_length=100, null=True)),
                ('hp_ketua_rt', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Nama rt',
                'verbose_name_plural': 'Nama rt',
            },
        ),
    ]