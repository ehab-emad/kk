# Generated by Django 4.2.10 on 2024-05-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0081_alter_workflow_object_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow_object',
            name='norman_reference',
            field=models.UUIDField(blank=True, editable=False, null=True, verbose_name='UUID NorMan'),
        ),
    ]
