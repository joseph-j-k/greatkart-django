# Generated by Django 5.2 on 2025-05-02 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
