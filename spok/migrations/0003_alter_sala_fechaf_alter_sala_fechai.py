# Generated by Django 5.1.2 on 2024-11-17 21:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spok', '0002_alter_sala_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='fechaf',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sala',
            name='fechai',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]