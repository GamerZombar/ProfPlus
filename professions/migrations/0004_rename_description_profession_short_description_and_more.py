# Generated by Django 4.1.5 on 2023-01-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0003_profession_title_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profession',
            old_name='description',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='profession',
            name='title_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/profession/img'),
        ),
    ]
