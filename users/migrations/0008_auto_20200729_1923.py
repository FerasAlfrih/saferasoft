# Generated by Django 3.0.7 on 2020-07-29 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_job_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='jobAs',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Job'),
        ),
    ]
