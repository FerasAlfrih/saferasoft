# Generated by Django 3.0.7 on 2020-07-09 20:49

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0002_auto_20200708_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='corona',
            name='countrypick',
            field=django_countries.fields.CountryField(default='null', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='corona',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
