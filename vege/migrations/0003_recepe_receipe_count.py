# Generated by Django 4.1.3 on 2023-09-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recepe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepe',
            name='receipe_count',
            field=models.IntegerField(default=1),
        ),
    ]