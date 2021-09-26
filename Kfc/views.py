from django.shortcuts import render, redirect
from Kfc.forms import OrderForm
from Kfc.models import Order
from django.contrib.auth import authenticate, login


def home(request):
    return render(request,'Kfc/home.html')
def register(request):
    return render(request,'Kfc/register.html')
def order_form(request):
    my_form=OrderForm()
    if request.method=='POST':
        my_form=OrderForm(request.POST)
        if my_form.is_valid():
            Order.objects.create(
                user=request.user,
                KFC_type=my_form.cleaned_data.get('pizza_type'),
                mobile=my_form.cleaned_data.get('mobile'),
                extra_item=my_form.cleaned_data.get('extra_item'),
                location=my_form.cleaned_data.get('location'),
            )
            my_form = OrderForm()
            return redirect('order_details')
    context={
        "form":my_form
    }
    return render(request,"Kfc/order.html",context)

def order_view(request):
    order_object=Order.objects.filter(user=request.user)
    context={
        'object':order_object,
    }
    return render(request,"Kfc/order_details.html",context)


