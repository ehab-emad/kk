# Generated by Django 4.2.7 on 2023-11-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='network_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
