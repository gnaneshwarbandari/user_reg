# Generated by Django 4.2.16 on 2024-09-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='course',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
