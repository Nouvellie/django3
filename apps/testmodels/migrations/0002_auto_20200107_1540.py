# Generated by Django 3.0.1 on 2020-01-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_choices',
            field=models.IntegerField(blank=True, choices=[(1, 'House'), (2, 'Car'), (3, 'Light'), (4, 'Buzz'), (5, 'Year'), (10, 'Star Patrick')], db_column='ITEM_CHOICES', default=1, null=True, verbose_name='CHOICES'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(blank=True, db_column='ITEM_NAME', max_length=50, null=True, unique=True, verbose_name='NAME'),
        ),
    ]
