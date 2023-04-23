# Generated by Django 4.2 on 2023-04-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phones',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.AlterField(
            model_name='phones',
            name='cost',
            field=models.CharField(max_length=100, null=True, verbose_name='Стоимость в $'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='фото:'),
        ),
    ]
