# Generated by Django 3.1.5 on 2021-02-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='bought',
            field=models.BooleanField(default=False),
        ),
    ]