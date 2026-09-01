from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Assistida, Evolucao
from .forms import AssistidaForm, EvolucaoForm

@login_required
def pagina_inicial(request):
    total_assistidas = Assistida.objects.count()
    return render(request, 'atendimentos/inicio.html', {'total_assistidas': total_assistidas})

@login_required
def lista_assistidas(request):
    query = request.GET.get('q', '') # Pega o termo digitado na busca
    
    if query:
        # Se a usuária digitou algo na busca, faz a filtragem por nome ou CPF
        assistidas = Assistida.objects.filter(nome_completo__icontains=query) | Assistida.objects.filter(cpf__icontains=query)
    else:
        # Se ninguém buscou nada, a lista fica vazia por padrão (sigilo e privacidade)
        assistidas = []
        
    return render(request, 'atendimentos/lista_assistidas.html', {'assistidas': assistidas, 'query': query})        

@login_required
def ver_ficha(request, id):
    assistida = get_object_or_404(Assistida, id=id)
    evolucoes = Evolucao.objects.filter(assistida=assistida).order_by('-data_atendimento')
    
    return render(request, 'atendimentos/ver_ficha.html', {
        'assistida': assistida, 
        'evolucoes': evolucoes
    })

@login_required
def nova_assistida(request):
    if request.method == 'POST':
        form = AssistidaForm(request.POST)
        if form.is_valid():
            nova_mulher = form.save()
            return redirect('ver_ficha', id=nova_mulher.id)
    else:
        form = AssistidaForm()
    
    return render(request, 'atendimentos/nova_assistida.html', {'form': form})

@login_required
def editar_assistida(request, id):
    assistida = get_object_or_404(Assistida, id=id)
    
    if request.method == 'POST':
        form = AssistidaForm(request.POST, instance=assistida)
        if form.is_valid():
            form.save()
            return redirect('ver_ficha', id=assistida.id)
    else:
        form = AssistidaForm(instance=assistida)
    
    return render(request, 'atendimentos/nova_assistida.html', {'form': form, 'assistida': assistida})

@login_required
def novo_atendimento(request, id):
    assistida = get_object_or_404(Assistida, id=id)
    
    if request.method == 'POST':
        form = EvolucaoForm(request.POST)
        if form.is_valid():
            evolucao = form.save(commit=False)
            evolucao.assistida = assistida 
            evolucao.save()
            return redirect('ver_ficha', id=assistida.id)
    else:
        form = EvolucaoForm()
        
    return render(request, 'atendimentos/novo_atendimento.html', {'form': form, 'assistida': assistida})

# NOVAS FUNÇÕES DE GESTÃO DE EQUIPE
@staff_member_required(login_url='login')
def gestao_equipe(request):
    usuarios = User.objects.all()
    return render(request, 'atendimentos/gestao_equipe.html', {'usuarios': usuarios})

@staff_member_required(login_url='login')
def novo_usuario(request):
    # Importar o form que criamos lá no forms.py
    from .forms import CadastroUsuarioForm 
    
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestao_equipe')
    else:
        form = CadastroUsuarioForm()
        
    return render(request, 'atendimentos/novo_usuario.html', {'form': form})

@staff_member_required(login_url='login')
def trocar_senha(request, id):
    usuario_alvo = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        form = SetPasswordForm(usuario_alvo, request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestao_equipe')
    else:
        form = SetPasswordForm(usuario_alvo)
        
   
    for field_name, field in form.fields.items():
        field.widget.attrs['class'] = 'form-control'
        
    return render(request, 'atendimentos/trocar_senha.html', {'form': form, 'usuario_alvo': usuario_alvo})

@staff_member_required(login_url='login')
def excluir_usuario(request, id):
    usuario_alvo = get_object_or_404(User, id=id)
    
    # Só exclui se for via POST (clique no botão) e se não for você mesmo
    if request.method == 'POST' and usuario_alvo != request.user:
        usuario_alvo.delete()
        
    return redirect('gestao_equipe')

@staff_member_required(login_url='login')
def excluir_assistida(request, id):
    assistida = get_object_or_404(Assistida, id=id)
    
    # Só exclui se a requisição for POST (vinda do clique no botão)
    if request.method == 'POST':
        assistida.delete()
        
    return redirect('lista_assistidas')