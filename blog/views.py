from django.shortcuts import render

from .models import Maqola, Intervyu


def home(request):
    return render(request, 'home.html')


def blog(request):
    data = {
        'maqolalar': Maqola.objects.all().order_by('-sana')
    }
    return render(request, 'blog.html', data)


def about(request):
    return render(request, 'about.html')

def maqola(request, pk):
    data = {
        'maqola': Maqola.objects.get(id=pk)
    }
    return render(request, 'maqola.html', data)


