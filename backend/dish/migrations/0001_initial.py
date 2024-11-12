# Generated by Django 5.1.3 on 2024-11-12 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0010_alter_restaurant_days_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]