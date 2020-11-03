# Generated by Django 3.1.2 on 2020-11-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_profile_hoodname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='neighborhood',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='business',
            field=models.ManyToManyField(to='hoodapp.Business'),
        ),
    ]