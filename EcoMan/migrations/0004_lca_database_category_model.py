# Generated by Django 4.2.7 on 2023-11-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoMan', '0003_remove_analysis_comparison_emissions_manufacturing_including_reuse'),
    ]

    operations = [
        migrations.AddField(
            model_name='lca_database',
            name='category_model',
            field=models.ManyToManyField(blank=True, default=None, to='EcoMan.lca_database_category', verbose_name='Categories'),
        ),
    ]
