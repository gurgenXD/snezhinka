# Generated by Django 2.2.1 on 2019-06-05 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190605_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsize',
            old_name='size',
            new_name='value',
        ),
    ]
