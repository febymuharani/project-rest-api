# Generated by Django 5.1 on 2024-09-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_kelompok_buku_kelompok_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='buku',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
