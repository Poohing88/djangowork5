# Generated by Django 2.2.1 on 2020-01-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200124_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletags',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
    ]
