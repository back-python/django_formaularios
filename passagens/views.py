from django.shortcuts import render
from passagens.forms import PassagemForms

# Create your views here.
def index(request):
    form = PassagemForms()

    context = {'form':form}

    return render(request, 'index.html', context)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            context = {'form':form}
            return render(request, 'minha_consulta.html', context)
        else:
            print('Formulário inválido')
            context = {'form':form}
            return render(request, 'index.html', context)