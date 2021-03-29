# Generated by Django 3.1.5 on 2021-03-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='Last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='purchase_quantity',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='reorder_level',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='sell_quantity',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]