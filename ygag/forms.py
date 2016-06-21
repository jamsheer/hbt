from django import forms

class NameForm(forms.Form):
    name_text = forms.CharField(label='Your name', max_length=200)