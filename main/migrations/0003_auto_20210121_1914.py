# Generated by Django 3.1.3 on 2021-01-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201213_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.IntegerField(null=True, verbose_name='Длина изделия'),
        ),
    ]
