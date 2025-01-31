# Generated by Django 4.2.10 on 2024-07-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoMan', '0022_analysis_settings_is_automotive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis_settings',
            name='is_automotive',
            field=models.BooleanField(default=True, verbose_name='Job functionality tailored as automotive application'),
        ),
    ]
