from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('assistidas/', views.lista_assistidas, name='lista_assistidas'),
    path('ficha/<int:id>/', views.ver_ficha, name='ver_ficha'),
    path('nova-assistida/', views.nova_assistida, name='nova_assistida'),
    path('editar/<int:id>/', views.editar_assistida, name='editar_assistida'),
    path('ficha/<int:id>/novo-atendimento/', views.novo_atendimento, name='novo_atendimento'),
    path('equipe/', views.gestao_equipe, name='gestao_equipe'),
    path('equipe/novo/', views.novo_usuario, name='novo_usuario'),
    path('equipe/senha/<int:id>/', views.trocar_senha, name='trocar_senha'),
    path('equipe/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    path('assistidas/excluir/<int:id>/', views.excluir_assistida, name='excluir_assistida'),
]