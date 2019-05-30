# Generated by Django 2.2.1 on 2019-05-30 16:11

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190530_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='products.SubCategory', verbose_name='Подкатегория'),
        ),
    ]
