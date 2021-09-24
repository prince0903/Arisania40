from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Atelier


def list_atelier(request):
    ateliers=Atelier.objects.all()
    context={'ateliers':ateliers}
    return render(request,'artisan_app/list_atelier.html',context)

def detail(request, atelier_id):
    atelier = Atelier.objects.get(id=atelier_id)
    context = {
        'atelier': atelier,
        }
    return render(request, 'artisan_app/detail.html', context)

