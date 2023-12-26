# Generated by Django 4.2.5 on 2023-12-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monolit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название товара')),
                ('ProductImage', models.ImageField(upload_to='productImages/', verbose_name='Изображение товара')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание товара')),
            ],
        ),
    ]