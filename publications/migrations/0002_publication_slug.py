# Generated by Django 5.0.6 on 2024-07-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
