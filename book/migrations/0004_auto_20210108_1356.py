# Generated by Django 3.1.4 on 2021-01-08 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210108_1335'),
        ('book', '0003_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='category.category'),
        ),
    ]
