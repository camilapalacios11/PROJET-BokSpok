# Generated by Django 5.1.2 on 2024-11-18 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spok', '0005_alter_sala_fechai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='fechai',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
