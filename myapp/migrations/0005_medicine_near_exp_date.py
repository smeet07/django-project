# Generated by Django 3.1.5 on 2021-03-25 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210325_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='near_exp_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]