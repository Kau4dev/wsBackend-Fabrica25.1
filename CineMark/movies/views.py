from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme, Favorito
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests


@login_required
def pagina_inicial(request):
    filmes_favoritos = Filme.objects.filter(favorito__usuario=request.user).distinct()
    return render(request, "movies/pagina_inicial.html", {"filmes_favoritos": filmes_favoritos})

@login_required
def busca(request):
    filmes = []
    filmes_favoritos_ids = Favorito.objects.filter(usuario=request.user).values_list("filme__id_imdb", flat=True)

    if request.method == "GET" and "entrada" in request.GET:
        entrada = request.GET["entrada"].strip()
        response = requests.get(f"https://www.omdbapi.com/?apikey=23140733&s={entrada}")
        
        if response.status_code == 200:
            dados = response.json()
            if dados.get("Response") == "True":
                filmes = dados.get("Search", [])

    return render(request, "movies/busca.html", {"filmes": filmes, "filmes_favoritos_ids": list(filmes_favoritos_ids)})

@login_required
def adicionar_filme_favorito(request, imdb_id):
    filme = Filme.objects.filter(id_imdb=imdb_id).first()

    if not filme:
        response = requests.get(f"http://www.omdbapi.com/?apikey=23140733&i={imdb_id}")

        if response.status_code == 200:
            dados = response.json()
            
            if dados.get("Response") == "True":
                ano = dados.get("Year")
                if ano:
                    ano = int(ano)
                else:
                    ano = 0

                filme = Filme.objects.create(
                    id_imdb=dados.get("imdbID"),
                    titulo=dados.get("Title"),
                    ano=ano,
                    poster=dados.get("Poster"),
                    sinopse=dados.get("Plot"),
                    usuario=request.user
                )
            else:
                return redirect('movies:busca')
    
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, filme=filme)

    return redirect('movies:pagina_inicial')

@login_required
def remover_filme_favorito(request, imdb_id):
    filme = get_object_or_404(Filme, id_imdb=imdb_id)
    favorito = get_object_or_404(Favorito, usuario=request.user, filme=filme)
    favorito.delete()
    return redirect("movies:pagina_inicial")
