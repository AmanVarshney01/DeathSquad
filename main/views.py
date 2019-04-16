from django.shortcuts import render
from .models import profiles
# Create your views here.

def home(request):
    context = {
        'profiles': profiles.objects.all()
    }
    return render(request, 'main/home.html', context)
