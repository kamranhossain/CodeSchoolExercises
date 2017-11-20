from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# ...
from .forms import LoginForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Other views not displayed.

def profile(request, username):
    request.user = User.objects.create_user('CodeSchool') # Temporary
    username = 'Code School'
    # locations = Location.objects.filter(user=user)
    locations = []
    return render(request, 'profile.html',
                  {'username': username,
                   'locations': locations})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                    #return Index(request)
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
        request.user = User.objects.create_user('CodeSchool')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
