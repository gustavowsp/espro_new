from django.urls import path
from vagas import views

app_name = 'vagas'


urlpatterns = [
    path('', views.index, name='homepage'),
    path('vaga/<int:id_vaga>', views.detalhes_vaga, name='detalhe-vaga'),
    path('criar/',views.criar_vaga, name='criar_vaga'),
]