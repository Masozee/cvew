# Generated by Django 4.0.5 on 2022-06-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_remove_incident_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='coordinate_type',
            field=models.CharField(choices=[(0, 'Polygon'), (1, 'MultiPolygon')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]