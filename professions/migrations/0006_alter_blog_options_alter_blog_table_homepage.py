# Generated by Django 4.1.5 on 2023-01-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0005_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterModelTable(
            name='blog',
            table='blog',
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='professions.profession', verbose_name='Профессия главной страницы')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главные страницы',
                'db_table': 'homepage',
            },
        ),
    ]
