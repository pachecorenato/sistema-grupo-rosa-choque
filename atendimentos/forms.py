from django import forms
from .models import Assistida, Evolucao

class AssistidaForm(forms.ModelForm):
    class Meta:
        model = Assistida
        # Pede para o Django criar o formulário com todos os campos do banco de dados
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Esse truque adiciona as classes do Bootstrap automaticamente 
        # para o formulário ficar bonito na tela sem muito esforço no HTML
        for field_name, field in self.fields.items():
            if type(field.widget) in [forms.CheckboxInput]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class EvolucaoForm(forms.ModelForm):
    class Meta:
        model = Evolucao
        fields = ['responsavel_tecnico', 'data_atendimento', 'formato_predominante', 'relato', 'proximo_passo', 'status_atual']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field.widget) in [forms.CheckboxInput]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroUsuarioForm(UserCreationForm):
   
    NIVEL_CHOICES = [
        ('', '--- Selecione o Nível de Acesso ---'),
        ('padrao', 'Voluntária Padrão'),
        ('admin', 'Coordenadora (Administradora)'),
    ]
    nivel_acesso = forms.ChoiceField(choices=NIVEL_CHOICES, label="Nível de Acesso", widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['username', 'nivel_acesso']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'nivel_acesso':
                field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):        
        user = super().save(commit=False)
        if self.cleaned_data['nivel_acesso'] == 'admin':
            user.is_staff = True
        else:
            user.is_staff = False
            
        if commit:
            user.save()
        return user