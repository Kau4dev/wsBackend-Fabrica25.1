from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('pagina_inicial', views.pagina_inicial, name='pagina_inicial'),
    path('busca', views.busca, name='busca'),
    path('remover_filme_favorito/<str:imdb_id>', views.remover_filme_favorito, name='remover_filme_favorito'),
    path('adicionar_filme_favorito/<str:imdb_id>', views.adicionar_filme_favorito, name='adicionar_filme_favorito'),
]
