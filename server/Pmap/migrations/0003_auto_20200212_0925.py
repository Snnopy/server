# Generated by Django 3.0.3 on 2020-02-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pmap', '0002_auto_20200211_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ugdr',
            field=models.BinaryField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='ustatus',
            field=models.IntegerField(default=1),
        ),
    ]