# Generated by Django 2.2 on 2020-12-14 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_app', '0005_auto_20201213_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quoted_by',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]