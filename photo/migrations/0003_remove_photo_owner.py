# Generated by Django 3.0.3 on 2020-02-14 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20200214_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
    ]
