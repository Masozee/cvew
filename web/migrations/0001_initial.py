# Generated by Django 4.0.5 on 2022-06-05 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=35)),
                ('keterangan', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Actor Category',
                'verbose_name_plural': 'Actor Categories',
            },
        ),
        migrations.CreateModel(
            name='distrcit_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', editable=False, max_length=320)),
                ('city_id', models.PositiveBigIntegerField(unique=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Kabupaten/Kota',
                'verbose_name_plural': 'Kabupaten/Kota',
            },
        ),
        migrations.CreateModel(
            name='incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.CharField(max_length=12)),
                ('slug', models.SlugField(default='', editable=False, max_length=320)),
                ('date', models.DateField()),
                ('covid_rel', models.PositiveBigIntegerField(null=True)),
                ('num_death', models.PositiveBigIntegerField(null=True)),
                ('num_injured', models.PositiveBigIntegerField(null=True)),
                ('death_injured', models.PositiveBigIntegerField(null=True)),
                ('fem_death', models.PositiveBigIntegerField(null=True)),
                ('fem_injured', models.PositiveBigIntegerField(null=True)),
                ('child_death', models.PositiveBigIntegerField(null=True)),
                ('child_injured', models.PositiveBigIntegerField(null=True)),
                ('Infra_damage', models.PositiveBigIntegerField(null=True)),
                ('Infra_destroyed', models.PositiveBigIntegerField(null=True)),
                ('intervene', models.CharField(choices=[('1', 'Ya'), ('2', 'Tidak'), ('0', 'Tidak Jelas')], max_length=2)),
                ('source', models.URLField()),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incident',
                'verbose_name_plural': 'Incidents',
            },
        ),
        migrations.CreateModel(
            name='Issue_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Issue Category',
                'verbose_name_plural': 'Issue Categories',
            },
        ),
        migrations.CreateModel(
            name='province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', editable=False, max_length=320)),
                ('province_id', models.PositiveIntegerField(unique=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Provinsi',
                'verbose_name_plural': 'Provinsi',
            },
        ),
        migrations.CreateModel(
            name='sub_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', editable=False, max_length=320)),
                ('subdistrict_id', models.PositiveBigIntegerField(unique=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.distrcit_city')),
            ],
            options={
                'verbose_name': 'Sub District',
                'verbose_name_plural': 'Sub District',
            },
        ),
        migrations.CreateModel(
            name='violence_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Violence Category',
                'verbose_name_plural': 'Violence Categories',
            },
        ),
        migrations.CreateModel(
            name='Weapon_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Weapon Category',
                'verbose_name_plural': 'Weapon Categories',
            },
        ),
        migrations.CreateModel(
            name='Weapon_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.weapon_category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.incident')),
            ],
            options={
                'verbose_name': 'Weapon Form',
                'verbose_name_plural': 'Weapon Forms',
            },
        ),
        migrations.CreateModel(
            name='violence_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.violence_category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.incident')),
            ],
            options={
                'verbose_name': 'Violence Form',
                'verbose_name_plural': 'Violence Forms',
            },
        ),
        migrations.CreateModel(
            name='village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', editable=False, max_length=320)),
                ('village_id', models.PositiveBigIntegerField(unique=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('sub_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.sub_district')),
            ],
            options={
                'verbose_name': 'Village',
                'verbose_name_plural': 'Village',
            },
        ),
        migrations.CreateModel(
            name='Issue_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.issue_category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.incident')),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
            },
        ),
        migrations.CreateModel(
            name='Intervene_actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_category', models.CharField(choices=[('0', 'Aktor Negara'), ('1', 'Aktor Non Negara'), ('2', 'Aktor Perusahaan Swasta')], max_length=2)),
                ('actor', models.CharField(max_length=150)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('incident_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.incident')),
            ],
            options={
                'verbose_name': 'Intervene',
                'verbose_name_plural': 'Intervene',
            },
        ),
        migrations.CreateModel(
            name='incident_actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', editable=False, max_length=320)),
                ('actor_no', models.CharField(blank=True, choices=[(1, 1), (2, 2)], max_length=1)),
                ('actor', models.CharField(max_length=100)),
                ('actor_category', models.CharField(choices=[('0', 'Aktor Negara'), ('1', 'Aktor Non Negara'), ('2', 'Aktor Perusahaan Swasta')], max_length=2)),
                ('actor_vm', models.CharField(choices=[('1', 'Ya'), ('2', 'Tidak'), ('0', 'Tidak Jelas')], max_length=2)),
                ('actor_Total', models.IntegerField()),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('incident_events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.incident')),
            ],
            options={
                'verbose_name': 'Incident Actor 1',
                'verbose_name_plural': 'Incident Actors 1',
            },
        ),
        migrations.AddField(
            model_name='incident',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.village'),
        ),
        migrations.AddField(
            model_name='incident',
            name='related',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.incident'),
        ),
        migrations.AddField(
            model_name='distrcit_city',
            name='Province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.province'),
        ),
    ]
