from dataclasses import fields
from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.tipo_classe import tipos_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa
from datetime import datetime

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida':'Data de ida', 'data_volta':'Data de volta', 'informacoes':'Informações', 'classe_viagem':'Classe do vôo'}
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker(),
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        origem_destino_iguais(origem, destino, lista_erros)
        campo_sem_numero(origem, 'origem', lista_erros)
        campo_sem_numero(destino, 'destino', lista_erros)
        data_ida_menor_que_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_que_data_atual(data_ida, data_pesquisa, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
        