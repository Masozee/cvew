# Generated by Django 4.0.5 on 2022-06-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_province_coordinate_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='coordinate_type',
            field=models.CharField(choices=[('0', 'Polygon'), ('1', 'MultiPolygon')], max_length=1),
        ),
    ]