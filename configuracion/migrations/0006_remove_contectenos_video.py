# Generated by Django 3.1.4 on 2021-05-12 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_auto_20210512_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contectenos',
            name='video',
        ),
    ]
