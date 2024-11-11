# Generated by Django 5.1.3 on 2024-11-11 03:05

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_restaurant_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='days_jobs',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sa', 'sabado'), ('vi', 'viernes'), ('mi', 'miercoles'), ('lu', 'lunes'), ('ma', 'martes'), ('ju', 'jueves'), ('do', 'domingo')], default='domingo', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
