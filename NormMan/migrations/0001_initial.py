# Generated by Django 4.2.7 on 2023-11-21 12:39

import NormMan.models.help_functions
import NormMan.models.normparts_shared_component
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormParts_Shared_Component',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('data_path', models.CharField(blank=True, max_length=50000, null=True)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('name_de', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, max_length=50000, null=True, upload_to=NormMan.models.normparts_shared_component.get_upload_to, verbose_name='Part Image')),
                ('stl_thumbnail', models.FileField(blank=True, max_length=50000, upload_to=NormMan.models.normparts_shared_component.get_upload_to)),
                ('file_catia_part', models.FileField(blank=True, max_length=50000, upload_to=NormMan.models.normparts_shared_component.get_upload_to)),
                ('file_configuration', models.FileField(blank=True, max_length=50000, upload_to=NormMan.models.normparts_shared_component.get_upload_to)),
                ('file_workflow_json', models.FileField(blank=True, max_length=5000, upload_to=NormMan.models.normparts_shared_component.get_upload_to)),
                ('counter', models.IntegerField(blank=True, default=0)),
                ('supplier_name', models.CharField(blank=True, max_length=200, null=True)),
                ('supplier_part_number', models.CharField(blank=True, max_length=200, null=True)),
                ('oem_reference_name', models.CharField(blank=True, max_length=200, null=True)),
                ('oem_reference_part_number', models.CharField(blank=True, max_length=200, null=True)),
                ('accessibility', models.CharField(choices=[('PRIVATE', 'Private'), ('DATABASE_USERS', 'Database Users'), ('PROJECT_USERS', 'Project Users')], default='private', max_length=50)),
                ('type', models.CharField(choices=[('COMPONENT', 'Component'), ('PART', 'Part'), ('SECTION', 'Section'), ('TEMPLATE', 'Template'), ('WORKFLOW', 'Workflow')], default='Component', max_length=50)),
                ('parameters', models.JSONField(blank=True, null=True, verbose_name='Catia Parameters')),
                ('material', models.CharField(blank=True, max_length=70, null=True)),
                ('source', models.CharField(blank=True, max_length=1000, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('density', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_NormMan_Ref',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser_NormMan_Ref',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('nickname', models.CharField(blank=True, default='Not defined', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_NormMan_Ref',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow_Session',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('workflow_status', models.JSONField(blank=True, null=True, verbose_name='workflow_status')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NormMan.projectuser_normman_ref')),
                ('workflow_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NormMan.normparts_shared_component', verbose_name='Parent Category of the Group')),
            ],
        ),
        migrations.AddField(
            model_name='normparts_shared_component',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NormMan.projectuser_normman_ref'),
        ),
        migrations.AddField(
            model_name='normparts_shared_component',
            name='project_model',
            field=models.ForeignKey(blank=True, default=None, help_text='Select a a project for Shared Component', on_delete=django.db.models.deletion.CASCADE, to='NormMan.project_normman_ref', verbose_name='Project'),
        ),
        migrations.CreateModel(
            name='Component_Group_Level',
            fields=[
                ('UUID', models.CharField(default=uuid.uuid4, editable=False, max_length=200, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(default='Not defined', max_length=100)),
                ('name_de', models.CharField(default='Not defined', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.CharField(blank=True, default='Put your comment here...', max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=NormMan.models.help_functions.get_upload_to, verbose_name='Part Image')),
                ('stl_thumbnail', models.FileField(blank=True, upload_to=NormMan.models.help_functions.get_upload_to)),
                ('data_path', models.FileField(blank=True, max_length=10000, upload_to='')),
                ('group_depth_level', models.IntegerField(default=0)),
                ('normparts_shared_components', models.ManyToManyField(blank=True, to='NormMan.normparts_shared_component', verbose_name='Shared Component')),
                ('parent_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NormMan.component_group_level', verbose_name='Parent Category of the Group')),
            ],
        ),
    ]
