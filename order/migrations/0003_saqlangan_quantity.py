# Generated by Django 3.2.13 on 2023-03-25 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_saqlangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='saqlangan',
            name='quantity',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]