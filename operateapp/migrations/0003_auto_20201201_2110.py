# Generated by Django 3.1.3 on 2020-12-01 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operateapp', '0002_auto_20201128_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='detail',
            new_name='article',
        ),
    ]
