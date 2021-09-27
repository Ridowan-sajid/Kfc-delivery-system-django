from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from UserReg.forms import UserRegisterForm


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'UserReg/registration.html', {'form': form})
