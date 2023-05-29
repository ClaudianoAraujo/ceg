from django.shortcuts import render
from .forms import UserForm
from .models import UsuarioManager, Usuario

# Create your views here.
def home(request):
    user = Usuario.objects.all()[:8]
    context = {'myuser':user}
    return render(request, 'index.html',context)


def create(request):
    return render(request, 'index.html')


def store(request):
    
    return render(request, 'form.html')


