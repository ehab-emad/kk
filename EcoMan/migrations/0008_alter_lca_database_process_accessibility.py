# Generated by Django 4.2.7 on 2023-11-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoMan', '0007_rename_category_model_lca_database_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lca_database_process',
            name='accessibility',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('DATABASE_USERS', 'Database Users'), ('HIDDEN', 'Hidden')], default='private', max_length=50),
        ),
    ]
