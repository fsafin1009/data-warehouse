# Generated by Django 3.1 on 2020-08-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200824_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категори'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-created_at'], 'verbose_name': 'Отчет', 'verbose_name_plural': 'Отчеты'},
        ),
        migrations.AddField(
            model_name='report',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Название категори'),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
