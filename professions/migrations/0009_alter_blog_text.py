# Generated by Django 4.1.5 on 2023-01-12 11:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0008_alter_blog_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
