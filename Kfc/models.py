from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    KFC_TYPE = (
        ('Triple Treat Meal', 'Triple Treat Meal'),
        ('Leg piece Bucket', 'Leg piece Bucket'),
        ('Delight Meal', 'Delight Meal'),
        ('Tacos Meal', 'Tacos Meal'),
    )
    KFC_type = models.CharField(max_length=20, choices=KFC_TYPE)
    mobile = models.IntegerField(max_length=11)
    ITEM = (
        ('Pespsi', 'Pespsi'),
        ('Coca Cola', 'Coca Cola'),
    )
    extra_item = models.CharField(max_length=20, choices=ITEM)
    location = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    DONE = (
        ('Not done', 'Not done'),
        ('Done', 'Done'),
    )
    done = models.CharField(max_length=10,choices=DONE, default='Not done')

    def __str__(self):
        return f'{self.user.username} {self.id}'
