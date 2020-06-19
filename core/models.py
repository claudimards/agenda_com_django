from django.db import models
from django.contrib.auth.models import User # importando usuarios do banco de dados

# Create your models here.

# método para criar um modelo de tabela para o banco de dados
class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    data_evento = models.DateTimeField(verbose_name = 'Data do Evento') #verbose modifica o nome apresentado na coluna na tabela
    data_criacao = models.DateTimeField(auto_now = True, verbose_name = 'Data de criação')
    # atribuindo usuario ao campo de chave estrangeira da tabela
    usuario = models.ForeignKey( User, on_delete = models.CASCADE ) # on_delete obriga a tabela a apagar todos registroso do usuario ao ser deletado

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo