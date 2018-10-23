# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from .forms import UserRegistrationForm, UserLoginForm, editProfile, avatarForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(
                    request, "Sorry, we are unable to log you in at this time, please try again later.")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('login'))
def profile(request):

    if request.method == 'POST':
        form = editProfile(request.POST, instance=request.user)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(
                request, "Password Updated")
            return redirect(reverse('profile'))
    else:
        form = editProfile()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'profile.html', args)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(
                    None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def new_avatar(request):
    if request.method =="POST":
        form=avatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = request.user
            user.save()
            messages.success(
                request, "Avatar Updated")
            return redirect(reverse('profile'))
    else:
        form = avatarForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'avatarForm.html', args)
