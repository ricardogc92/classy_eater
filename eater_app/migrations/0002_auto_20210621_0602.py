# Generated by Django 2.2 on 2021-06-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eater_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
