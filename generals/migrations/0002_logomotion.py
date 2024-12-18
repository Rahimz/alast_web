# Generated by Django 5.0.6 on 2024-11-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoMotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('file', models.FileField(help_text='Just upload video files', upload_to='generals/logo/', verbose_name='File')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
