from django.db import models

# Create your models here.
# A classe do model equivale a uma tabela do banco de dados
class Questao(models.Model):
    pergunta = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pergunta


class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.resposta # Vai retornar a resposta que eu pedi, com o id que eu coloquei, posso pedir qualquer campo