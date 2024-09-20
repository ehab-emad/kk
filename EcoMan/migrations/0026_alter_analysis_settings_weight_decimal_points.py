# Generated by Django 4.2.14 on 2024-09-02 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoMan', '0025_alter_analysis_settings_is_automotive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis_settings',
            name='weight_decimal_points',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='Decimal Points For Weight'),
        ),
    ]
