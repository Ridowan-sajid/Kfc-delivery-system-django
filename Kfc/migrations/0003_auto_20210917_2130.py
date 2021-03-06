# Generated by Django 3.2.7 on 2021-09-17 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Kfc', '0002_order_extra_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pizza_type',
            field=models.CharField(choices=[('Triple Treat Meal', 'Triple Treat Meal'), ('Leg piece Bucket', 'Leg piece Bucket'), ('Delight Meal', 'Delight Meal'), ('Tacos Meal', 'Tacos Meal')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
