# Generated by Django 5.1 on 2024-08-15 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discoint',
            new_name='discount',
        ),
    ]
