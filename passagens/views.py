from django.shortcuts import render
from passagens.forms import PassagemForms

# Create your views here.
def index(request):
    form = PassagemForms()

    context = {'form':form}

    return render(request, 'index.html', context)