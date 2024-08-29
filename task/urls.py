from django.urls import path
from .views import home_views,user_views,roupa_views


urlpatterns = [
    path('cadastrar/usuario',view=user_views.adicionar_usuario,name='adicionar_usuario'),
    path('login',view=user_views.autenticar_usuario,name='autenticar_usuario'),
    path('home', view=home_views.home,name='home'),
    path ('listar/produto',view=roupa_views.lista_produtos,name='listar_produto'),
    path ('cadastrar/produto',view=roupa_views.cadastrar_produto,name='cadastrar_produto'),

    path('produto/<int:pk>/', view=roupa_views.roupa_views,name='descricao_roupa'),
]

