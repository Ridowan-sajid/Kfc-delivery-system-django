# Generated by Django 3.2.7 on 2021-09-26 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kfc', '0012_alter_order_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pizza_type',
            new_name='KFC_type',
        ),
    ]
