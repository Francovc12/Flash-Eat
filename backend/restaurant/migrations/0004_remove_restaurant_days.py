# Generated by Django 5.1.3 on 2024-11-11 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='days',
        ),
    ]
