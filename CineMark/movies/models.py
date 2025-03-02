from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    id_imdb = models.CharField(max_length=20)
    titulo = models.CharField(max_length=255)
    ano = models.IntegerField()
    poster = models.URLField()
    sinopse = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.first_name} - {self.filme.titulo}"
    
