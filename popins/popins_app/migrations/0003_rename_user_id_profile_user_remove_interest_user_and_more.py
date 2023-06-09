# Generated by Django 4.1.7 on 2023-04-09 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('popins_app', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='interest',
            name='nanny',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='interests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='nanny',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='session',
            name='interested_nannys',
            field=models.ManyToManyField(related_name='sessions', through='popins_app.Interest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='interest',
            name='session',
        ),
        migrations.AlterField(
            model_name='interest',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='interest',
            name='talked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='session',
            table=None,
        ),
        migrations.AddField(
            model_name='interest',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='popins_app.session'),
        ),
    ]
