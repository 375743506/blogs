# Generated by Django 3.1.3 on 2020-11-30 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20201130_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='mainapp.cate', verbose_name='所属类别'),
        ),
    ]