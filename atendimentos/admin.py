from django.contrib import admin
from .models import Assistida, Evolucao

@admin.register(Assistida)
class AssistidaAdmin(admin.ModelAdmin):
    # Adicionamos o 'id' aqui para aparecer na lista geral
    list_display = ('id', 'nome_completo', 'telefone', 'data_cadastro')
    search_fields = ('nome_completo', 'cpf')
    
    # Dizemos ao Django que o 'id' e a 'data_cadastro' são apenas para leitura
    readonly_fields = ('id', 'data_cadastro')
    
    fieldsets = (
        ('DADOS IDENTIFICADORES (SIGILO ABSOLUTO)', {
            'fields': (
                'id', 
                'data_cadastro',
                'nome_completo', 'data_nascimento', 'cpf', 'telefone', 
                'seguro_receber_mensagens', 'email', 'melhor_horario', 'endereco'
            )
        }),
        ('PERFIL DA SITUAÇÃO DE VIOLÊNCIA', {
            'fields': (
                ('violencia_fisica', 'violencia_psicologica', 'violencia_sexual'),
                ('violencia_patrimonial', 'violencia_moral', 'violencia_virtual'),
                'tipo_agressor', 'qual_agressor_outro', 
                'risco_imediato', 'medida_protetiva'
            )
        }),
        ('ESCOPO DO ATENDIMENTO REMOTO', {
            'fields': (
                ('apoio_psicologico', 'orientacao_juridica', 'assistencia_social'),
                'local_seguro'
            )
        }),
    )

@admin.register(Evolucao)
class EvolucaoAdmin(admin.ModelAdmin):
    list_display = ('assistida', 'data_atendimento', 'responsavel_tecnico', 'status_atual')
    search_fields = ('assistida__nome_completo',)
    
    fieldsets = (
        ('IDENTIFICAÇÃO E FORMATO', {
            'fields': ('assistida', 'responsavel_tecnico', 'data_atendimento', 'formato_predominante')
        }),
        ('HISTÓRICO DE EVOLUÇÃO E ATENDIMENTOS', {
            'fields': ('relato', 'proximo_passo')
        }),
        ('ENCAMINHAMENTOS RECENTES E ARTICULAÇÃO EM REDE', {
            'fields': (
                ('enc_deam', 'enc_defensoria', 'enc_cras'),
                ('enc_saude', 'enc_caps', 'enc_abrigo'),
                'observacoes_encaminhamento'
            )
        }),
        ('STATUS ATUAL', {
            'fields': ('status_atual',)
        }),
    )