# Generated by Django 4.1.3 on 2022-11-04 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApi', '0008_remove_projects_langugeandtool_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='languageAndTool',
        ),
        migrations.AddField(
            model_name='projects',
            name='LangugeAndTool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApi.languge'),
        ),
    ]