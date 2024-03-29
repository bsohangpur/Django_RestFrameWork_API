# Generated by Django 4.1.3 on 2022-12-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApi', '0015_rename_images_image_url_image_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
