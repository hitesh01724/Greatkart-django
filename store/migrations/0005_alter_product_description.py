# Generated by Django 4.0.1 on 2022-02-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_delete_myvar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
