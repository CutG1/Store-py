# Generated by Django 4.2.1 on 2024-01-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Link video'),
        ),
    ]
