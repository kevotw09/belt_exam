# Generated by Django 2.2 on 2020-12-14 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quote_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_by_user', to='quote_app.User')),
                ('user_like', models.ManyToManyField(related_name='liked_quote', to='quote_app.User')),
            ],
        ),
    ]
