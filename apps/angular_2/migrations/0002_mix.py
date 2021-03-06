# Generated by Django 3.0.1 on 2020-01-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angular_2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('mix_id', models.AutoField(db_column='MIX_ID', primary_key=True, serialize=False, verbose_name='MIX_ID')),
                ('images_id', models.ForeignKey(blank=True, db_column='IMAGES_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='angular_2.Images', verbose_name='IMAGES_ID')),
                ('testing_id', models.ForeignKey(blank=True, db_column='TESTING_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='angular_2.Testing', verbose_name='TESTING_ID')),
            ],
        ),
    ]
