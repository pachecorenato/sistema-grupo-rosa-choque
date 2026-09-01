# Sistema Rosa Choque

Um sistema web de gestão de atendimentos e prontuários desenvolvido para a ONG Grupo Rosa Choque. O projeto visa digitalizar, organizar e proteger as informações de mulheres atendidas pela instituição, fornecendo uma plataforma segura para as voluntárias e coordenadoras.

## Objetivo do Projeto
Desenvolver uma aplicação robusta e amigável que substitua o uso de planilhas de papel, garantindo o sigilo absoluto dos dados sensíveis e facilitando a gestão do histórico de evoluções de cada atendida. Este projeto foi desenvolvido como requisito acadêmico e demonstra a aplicação prática da arquitetura MVT (Model-View-Template).

## Principais Funcionalidades

*   **Gestão de Prontuários (CRUD):** Cadastro completo de atendidas, incluindo dados pessoais, informações sobre o agressor, análise de risco imediato e medidas protetivas.
*   **Histórico de Evoluções:** Registro cronológico de cada atendimento realizado, vinculando as ações tomadas ao prontuário da atendida.
*   **Sistema de Autenticação Seguro:** Login e Logout protegidos pelo ecossistema nativo do Django, com senhas criptografadas (hash).
*   **Controle de Níveis de Acesso (RBAC):** 
    *   *Voluntária Padrão:* Pode cadastrar e visualizar fichas e evoluções.
    *   *Coordenadora (Staff):* Possui acesso exclusivo à Gestão de Equipe, podendo criar novos usuários, redefinir senhas esquecidas e excluir prontuários e contas (exclusão lógica e em cascata).
*   **Interface Responsiva e Intuitiva:** Telas limpas e adaptáveis para uso em computadores da instituição, prevenindo erros de operação.

## Tecnologias Utilizadas

*   **Back-end:** Python 3, Django 5.x
*   **Banco de Dados:** SQLite (com persistência de dados local/nuvem)
*   **Front-end:** HTML5, CSS3, Bootstrap 5 (Estilização e Responsividade)
*   **Segurança:** Proteção CSRF em todos os formulários, Decorators de restrição de acesso (`@login_required`, `@staff_member_required`).

## Como executar o projeto localmente

Siga os passos abaixo para rodar o sistema na sua máquina:

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/sistema-rosa-choque.git

2. Entre na pasta do projeto:
   ```bash
   cd sistema-rosa-choque

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate

5. Crie um superusuário para acessar o sistema pela primeira vez:
   ```bash
   python manage.py createsuperuser

6. Inicie o servidor local:
   ```bash
   python manage.py runserver

7. Acesse no navegador: http://127.0.0.1:8000


**Lembrete:** No código acima, lá no Passo 1 da execução, lembre-se de trocar `SEU_USUARIO` pelo seu nome de usuário real do GitHub.




 
  
