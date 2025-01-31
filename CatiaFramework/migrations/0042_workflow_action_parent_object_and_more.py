# Generated by Django 4.2.7 on 2024-02-01 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0041_remove_workflow_action_comment_section_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow_action',
            name='parent_object',
            field=models.ForeignKey(blank=True, default=None, help_text='Parent Dependent Object', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_Object_Parent', to='CatiaFramework.workflow_object', verbose_name='Parent Object'),
        ),
        migrations.AlterField(
            model_name='workflow_action',
            name='parent_action',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_Action_Parent', to='CatiaFramework.workflow_action', verbose_name='Parent Action'),
        ),
    ]
