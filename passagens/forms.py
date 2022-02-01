from django import forms

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=200)
    destino = forms.CharField(label='Destino', max_length=200)
    data_ida = forms.DateField(label='Data de ida')
    data_volta = forms.DateField(label='Data de volta')