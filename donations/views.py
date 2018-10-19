# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import donateForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required
def donation(request):
    if request.method == "POST":
        form = donateForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=499,
                    currency="GBP",
                    description=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                    statement_descriptor="PC HOBBYIST DONATION"
                )
                if customer.paid:
                    messages.success(request, "Thank you for your donation!")
                    return redirect(reverse('profile'))
                else:
                    messages.error(
                        request, "An error has occurred, please check your card details and try again.")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        form = donateForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'donationForm.html', args)
