# Generated by Django 3.0.6 on 2021-02-08 10:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210207_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='photo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/static', location='/Users/ivanderjmw/Projects/teleteam-heroku/staticfiles'), upload_to='group-photos/'),
        ),
    ]
