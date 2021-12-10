from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegistrationforms


def homePage(request):

    return render(request, 'app/home.html', )


def registerPage(request):
    form = UserRegistrationforms()
    if request.method == "POST":
        form = UserRegistrationforms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username} your account has been created successfully')

        else:
            form = UserRegistrationforms()
            messages.error(request,
                           ' Failed to create your account. Please check your details')

    return render(request, 'app/register.html', {'form': form})


def profilePage(request):
    return render(request, 'app/accounts/profile.html')
