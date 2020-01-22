# Generated by Django 3.0.1 on 2020-01-18 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('testing_id', models.AutoField(db_column='TESTING_ID', primary_key=True, serialize=False, verbose_name='TESTING_ID')),
                ('testing_name', models.TextField(blank=True, db_column='TESTING_NAME', null=True, verbose_name='NAME')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('images_id', models.AutoField(db_column='IMAGES_ID', primary_key=True, serialize=False, verbose_name='IMAGES_ID')),
                ('images_url', models.URLField(blank=True, db_column='IMAGES_URL', max_length=800, null=True, verbose_name='URL')),
                ('testing_id', models.ForeignKey(blank=True, db_column='TESTING_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='angular_2.Testing', verbose_name='TESTING_ID')),
            ],
        ),
    ]