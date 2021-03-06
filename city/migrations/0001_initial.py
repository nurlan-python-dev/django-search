# Generated by Django 4.0.5 on 2022-06-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='Mamlakat nomi', max_length=255, verbose_name='Mamlakat')),
                ('iso', models.CharField(help_text='ISO', max_length=3, verbose_name='ISO (Alpha-3 code)')),
                ('city', models.CharField(help_text='Poytaxt', max_length=255, verbose_name='Poytaxt nomi')),
                ('time_zone', models.CharField(help_text='Vaqt zona', max_length=255, verbose_name='Vaqt zonasi')),
            ],
            options={
                'verbose_name': 'Shahar ',
                'verbose_name_plural': 'Shaharlar',
            },
        ),
    ]
