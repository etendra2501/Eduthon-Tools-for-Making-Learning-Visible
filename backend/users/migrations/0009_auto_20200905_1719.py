# Generated by Django 3.0.6 on 2020-09-05 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200905_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
