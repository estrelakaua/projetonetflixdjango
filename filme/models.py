from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ('ACAO', 'Ação'),
    ('COMEDIA', 'Comédia'),
    ('DESENHO', 'Desenho'),
    ('OUTROS', 'Outros'),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    visualizacoes = models.IntegerField(default=0)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    data_criacao = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_filmes')

    def __str__(self):
        return self.titulo


#criar episodios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')


# criar o usuário