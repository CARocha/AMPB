# Generated by Django 3.1.1 on 2020-11-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_quienessomos_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='quienessomos',
            name='orden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]