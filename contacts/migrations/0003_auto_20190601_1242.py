# Generated by Django 2.2.1 on 2019-06-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_mapcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapcode',
            name='map_code',
            field=models.TextField(verbose_name='Карта'),
        ),
    ]
