# Generated by Django 3.1.1 on 2020-11-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_quienessomos_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quienessomos',
            name='orden',
            field=models.IntegerField(unique=True),
        ),
    ]
