# Generated by Django 2.2.1 on 2019-06-16 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_aboutus_ourpros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]
