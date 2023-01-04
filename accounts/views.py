from django.shortcuts import render
from .models import Cliente, Nutri
from .forms import ClienteSignupForm, NutriSignupForm


def signup(request):
    clienteform = ClienteSignupForm()
    nutriform = NutriSignupForm()
    return render(request, 'registration/signup.html', {
        'form': nutriform
    })
    