# Generated by Django 2.0.3 on 2019-12-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ins',
            name='date',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='spends',
            name='date',
            field=models.CharField(max_length=15),
        ),
    ]
