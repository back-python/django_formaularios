from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.tipo_classe import tipos_classe
from datetime import datetime

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=200)
    destino = forms.CharField(label='Destino', max_length=200)
    data_ida = forms.DateField(label='Data de ida', widget=DatePicker())
    data_volta = forms.DateField(label='Data de volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    tipo_classe = forms.ChoiceField(label='Tipo de vôo', choices=tipos_classe)
    observacoes = forms.CharField(label='Observações', max_length=200, widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=150)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('O campo origem não pode contem números!')
        else:
            return origem
