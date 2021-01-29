from django import forms
from .models import Leads

class QuotationForm(forms.Form):
    your_name = forms.CharField(label='Name', max_length=30)
    # budget = forms.IntegerField(label='budget')
    email = forms.EmailField(label='email', max_length=254)
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='describe your project'
    )

