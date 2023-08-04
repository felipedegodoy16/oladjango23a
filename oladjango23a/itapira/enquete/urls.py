from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('felipe', views.caneta, name='caneta'),
    # ex: /enquete/número da questão
    path("<int:pk>/", views.DetalheView.as_view(), name="detalhe"),
    # ex: /enquete/número da questão/resultados
    path("<int:pk>/resultados/", views.ResultadoView.as_view(), name="resultados"),
    # ex: /enquete/número da questão/voto 
    path("<int:questao_id>/voto/", views.voto, name="voto"),
]