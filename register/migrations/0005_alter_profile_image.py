# Generated by Django 3.2.6 on 2021-09-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/home/chinmay/projects/django/LostAndFound/media/default.jpg', upload_to='register/images'),
        ),
    ]
