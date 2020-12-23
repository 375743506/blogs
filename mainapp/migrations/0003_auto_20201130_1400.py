# Generated by Django 3.1.3 on 2020-11-30 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201128_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='article',
            name='name',
        ),
        migrations.AddField(
            model_name='article',
            name='adesc',
            field=models.TextField(default='', verbose_name='文章描述'),
        ),
        migrations.AddField(
            model_name='article',
            name='aname',
            field=models.CharField(default='新文章', max_length=20, verbose_name='文章名字'),
        ),
        migrations.AlterField(
            model_name='cate',
            name='desc',
            field=models.TextField(default='', verbose_name='类别描述'),
        ),
    ]
