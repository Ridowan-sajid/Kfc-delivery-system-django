# Generated by Django 3.2.7 on 2021-09-17 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kfc', '0007_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
