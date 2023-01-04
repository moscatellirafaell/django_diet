from django import forms

class ClienteSignupForm(forms.Form):
    nome = forms.CharField(label='Nome')
    sobrenome = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='Email')


class NutriSignupForm(ClienteSignupForm):
    crn = forms.CharField(label='CRN')
    