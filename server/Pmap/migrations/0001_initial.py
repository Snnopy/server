# Generated by Django 3.0.3 on 2020-02-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, unique=True)),
                ('upwd', models.CharField(max_length=30)),
            ],
        ),
    ]
