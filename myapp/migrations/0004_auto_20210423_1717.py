# Generated by Django 3.1.5 on 2021-04-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_medicinehistory_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='activate',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]