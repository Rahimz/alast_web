# Generated by Django 5.0.6 on 2024-09-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_teammember_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='behance',
            field=models.URLField(blank=True, null=True, verbose_name='Behance'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin'),
        ),
    ]
