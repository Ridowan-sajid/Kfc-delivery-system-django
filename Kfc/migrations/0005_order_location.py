# Generated by Django 3.2.7 on 2021-09-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kfc', '0004_remove_order_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]