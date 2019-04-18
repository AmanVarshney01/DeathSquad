from django.shortcuts import render
from .models import profiles
from .forms import joinsquadform
# Create your views here.

def home(request):
    form = joinsquadform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'profiles': profiles.objects.all(),
        'form': form,
    }
    return render(request, 'main/home.html', context)
