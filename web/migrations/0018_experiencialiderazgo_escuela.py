# Generated by Django 3.1.4 on 2021-08-18 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20210517_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencialiderazgo',
            name='escuela',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.escuela'),
        ),
    ]