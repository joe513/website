# Generated by Django 2.0.2 on 2018-02-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180219_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Number'),
        ),
    ]