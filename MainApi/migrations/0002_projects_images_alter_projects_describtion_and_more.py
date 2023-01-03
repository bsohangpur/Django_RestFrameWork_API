# Generated by Django 4.0.2 on 2022-10-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='images',
            field=models.ImageField(default='', upload_to='MainApi/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='describtion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='langAndTool',
            field=models.CharField(choices=[('React', 'React'), ('Django', 'React'), ('Next', 'React')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
