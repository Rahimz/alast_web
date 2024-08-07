# Generated by Django 5.0.6 on 2024-07-26 15:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sub title')),
                ('authors', models.CharField(max_length=350, verbose_name='Authors')),
                ('abstract', models.TextField(blank=True, verbose_name='Abstract')),
                ('pdf', models.FileField(upload_to='publications/pdf/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='PDF file')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
