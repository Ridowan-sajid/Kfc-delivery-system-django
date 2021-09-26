from django import forms
from Kfc.models import Order

class OrderForm(forms.Form):
    KFC_TYPE = (
        ('Triple Treat Meal','Triple Treat Meal'),
        ('Leg piece Bucket','Leg piece Bucket'),
        ('Delight Meal','Delight Meal'),
        ('Tacos Meal','Tacos Meal'),
    )
    ITEM = (
        ('Pespsi','Pespsi'),
        ('Coca Cola','Coca Cola'),
    )
    KFC_type= forms.ChoiceField(choices=KFC_TYPE)
    mobile=forms.CharField()
    extra_item = forms.ChoiceField(choices=ITEM)
    location=forms.CharField()


