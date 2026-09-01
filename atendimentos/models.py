from django.db import models

class Assistida(models.Model):
    OPCAO_SIM_NAO = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    # DADOS IDENTIFICADORES
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo / Nome Social")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=14, blank=True, verbose_name="CPF")
    telefone = models.CharField(max_length=20, verbose_name="Telefone/WhatsApp")
    
    # Opções Sim/Não
    seguro_receber_mensagens = models.CharField(
        max_length=3, 
        choices=OPCAO_SIM_NAO, 
        default='sim', 
        verbose_name="É seguro receber mensagens?"
    )
    
    email = models.EmailField(blank=True, verbose_name="E-mail")
    melhor_horario = models.CharField(max_length=50, blank=True, verbose_name="Melhor horário para contato")
    endereco = models.TextField(blank=True, verbose_name="Endereço Residencial (Opcional)")

    # PERFIL DA SITUAÇÃO DE VIOLÊNCIA (Booleanos para marcar caixinhas)
    violencia_fisica = models.BooleanField(default=False, verbose_name="Física")
    violencia_psicologica = models.BooleanField(default=False, verbose_name="Psicológica")
    violencia_sexual = models.BooleanField(default=False, verbose_name="Sexual")
    violencia_patrimonial = models.BooleanField(default=False, verbose_name="Patrimonial")
    violencia_moral = models.BooleanField(default=False, verbose_name="Moral")
    violencia_virtual = models.BooleanField(default=False, verbose_name="Virtual / Stalking")

    AGRESSOR_CHOICES = [
        ('', '--- Selecione o Agressor ---'),
        ('conjugue', 'Cônjuge/Companheiro(a)'),
        ('ex_parceiro', 'Ex-parceiro(a)'),
        ('familiar', 'Familiar'),
        ('outro', 'Outro'),
    ]
    tipo_agressor = models.CharField(max_length=50, choices=AGRESSOR_CHOICES, blank=True, verbose_name="Quem é o agressor?")
    qual_agressor_outro = models.CharField(max_length=100, blank=True, verbose_name="Outro agressor (especificar)")

    RISCO_CHOICES = [
        ('', '--- Selecione o Risco ---'),
        ('alto', 'Sim, risco alto'),
        ('moderado', 'Sim, risco moderado'),
        ('nao', 'Não no momento'),
    ]
    risco_imediato = models.CharField(max_length=20, choices=RISCO_CHOICES, blank=True, verbose_name="Existe risco imediato à integridade física ou à vida?")

    MEDIDA_CHOICES = [
        ('', '--- Selecione a Medida Protetiva ---'),
        ('sim', 'Sim'),
        ('nao', 'Não'),
        ('desejo', 'Desejo solicitar'),
    ]
    medida_protetiva = models.CharField(max_length=20, choices=MEDIDA_CHOICES, blank=True, verbose_name="Possui Medida Protetiva de Urgência ativa?")

    # ESCOPO DO ATENDIMENTO REMOTO
    apoio_psicologico = models.BooleanField(default=False, verbose_name="Apoio Psicológico")
    orientacao_juridica = models.BooleanField(default=False, verbose_name="Orientação Jurídica")
    assistencia_social = models.BooleanField(default=False, verbose_name="Assistência Social")
    local_seguro = models.CharField(
        max_length=3, 
        choices=OPCAO_SIM_NAO, 
        default='sim', 
        verbose_name="Possui local reservado e seguro para as videochamadas?"
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data do Cadastro Inicial")

    def __str__(self):
        # Vai mostrar "Número Prontuário  - Nome" nas listas
        return f"Prontuário {self.id} - {self.nome_completo}"


class Evolucao(models.Model):
    assistida = models.ForeignKey(Assistida, on_delete=models.CASCADE, verbose_name="Assistida")
    responsavel_tecnico = models.CharField(max_length=100, verbose_name="Responsável Técnico Atual")
    data_atendimento = models.DateTimeField(verbose_name="Data e Hora do Atendimento")

    MODALIDADE_CHOICES = [
        ('online', 'Online'),
        ('presencial', 'Presencial'),
        ('hidrido', 'Híbrido'),
    ]
    formato_predominante = models.CharField(max_length=20, choices=MODALIDADE_CHOICES, default='online', verbose_name="Formato Predominante")

    relato = models.TextField(verbose_name="Evolução do Caso, Relato e Intervenções Realizadas")
    proximo_passo = models.CharField(max_length=200, blank=True, verbose_name="Próximo Passo / Agendamento")

    # ENCAMINHAMENTOS RECENTES (Caixinhas)
    enc_deam = models.BooleanField(default=False, verbose_name="DEAM / Delegacia da Mulher")
    enc_defensoria = models.BooleanField(default=False, verbose_name="Defensoria Pública / Jurídico")
    enc_cras = models.BooleanField(default=False, verbose_name="Cras / Creas / Assist. Social")
    enc_saude = models.BooleanField(default=False, verbose_name="Unidade de Saúde / Hospital")
    enc_caps = models.BooleanField(default=False, verbose_name="Caps / Saúde Mental")
    enc_abrigo = models.BooleanField(default=False, verbose_name="Casa de Abrigo / Acolhimento")
    observacoes_encaminhamento = models.TextField(blank=True, verbose_name="Outros / Observações do encaminhamento")

    STATUS_CHOICES = [
        ('ativo', 'Em atendimento ativo'),
        ('suspenso', 'Caso suspenso temporariamente'),
        ('alta', 'Processo de desligamento / Alta'),
    ]
    status_atual = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo', verbose_name="Status Atual do Acompanhamento")

    def __str__(self):
        return f"{self.assistida.nome_completo} - {self.data_atendimento.strftime('%d/%m/%Y')}"