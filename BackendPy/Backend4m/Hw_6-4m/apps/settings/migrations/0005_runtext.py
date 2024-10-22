# Generated by Django 4.2.7 on 2024-09-30 12:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runtext', ckeditor.fields.RichTextField(verbose_name='бег-строка')),
            ],
            options={
                'verbose_name_plural': 'Бег_строка',
            },
        ),
    ]
