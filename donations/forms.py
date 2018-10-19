from django import forms

class donateForm(forms.Form):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2018, 2039)]

    credit_card_number = forms.CharField(label='Credit Card Number', help_text="Please enter your 16-digit card number")
    cvv = forms.CharField(label='Security Code (CVV)', help_text="Please enter the last 3 digits of the security code on the back of your card.")
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, help_text="Please enter the card exipiry month")
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, help_text="Please enter the card exipiry year")
    stripe_id = forms.CharField(widget=forms.HiddenInput)
