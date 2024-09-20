# Generated by Django 4.2.10 on 2024-05-08 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0077_workflow_action_is_for_all_instances'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow_object',
            name='reference_instance',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objects_referenced_instances', to='CatiaFramework.workflow_object', verbose_name='Reference to instance in other session'),
        ),
        migrations.AlterField(
            model_name='workflow_object',
            name='type',
            field=models.CharField(choices=[('INSTANCE', 'Instance'), ('REFERENCE', 'Reference'), ('TEMPLATE', 'Template'), ('FRAMEWORK_INTERNAL', 'Framework Internal')], default='STAGE', max_length=50),
        ),
    ]
