# Generated by Django 4.1.7 on 2023-04-14 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popins_app', '0007_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]