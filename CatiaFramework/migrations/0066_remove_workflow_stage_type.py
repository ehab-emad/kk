# Generated by Django 4.2.10 on 2024-03-06 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0065_workflow_object_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflow_stage',
            name='type',
        ),
    ]
