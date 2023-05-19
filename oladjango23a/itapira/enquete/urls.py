from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('felipe', views.caneta, name='caneta'),
    # ex: /enquete/número da questão
    path("<int:questao_id>/", views.detalhe, name="detalhe"),
    # ex: /enquete/número da questão/resultados
    path("<int:questao_id>/resultados/", views.resultados, name="resultados"),
    # ex: /enquete/número da questão/voto 
    path("<int:questao_id>/voto/", views.voto, name="voto"),
]