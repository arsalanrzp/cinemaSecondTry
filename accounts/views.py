from audioop import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserRegisterForms
from django.contrib import messages
# Create your views here.
from django.urls import reverse


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise Http404()
        else:
            login(request, user)
            messages.success(request, f'successfully logged in !!')
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))

    else:
        if request.user.is_authenticated:
            response = request.user.get_full_name()
            return HttpResponse(response + ", you're already logged in")
        else:
            return render(request, 'accounts/loginpage.html', {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


@login_required
def profile_details(request):
    profile = request.user.profile
    return HttpResponse(profile)

def registerform(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            newuser = form.save(commit=False)
            newuser.set_password(newuser.password)
            # newuser.is_staff = True
            newuser.save()

    else:
        form = UserRegisterForms()
    context = {
    'form': form
    }
    return render(request, 'accounts/register.html', context)
