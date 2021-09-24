from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def inscriptionPage(request):
    form=UserCreationForm(request.POST)
    context={'form':form}

    return render(request,'compte/inscription.html',context)

def login(request):
    context={}

    return render(request,'compte/login.html',context)