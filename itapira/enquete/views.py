from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Criando função no python, se usa def = definição
# Parâmetro é o valor que passo pra função
# Passar um request padrão dentro dos parênteses
# Python abre blocos com ':'
# Sempre usar 4 espaços para identar, não misturar 4 espaços com tab

def index(request):
    return HttpResponse("<h1>Olha, se você não me ama</h1><h2>Caneta azul, azul caneta</h2>")
