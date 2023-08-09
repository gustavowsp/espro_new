from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from vagas.models import Vaga


def index(request):

  vagas = Vaga.objects.all()

  return render(request,'vagas/index.html',{
    'vagas' : vagas
  })

def detalhes_vaga(request,id_vaga):

  try:
    vaga = Vaga.objects.get(id=id_vaga)
  except:
    return redirect('vagas:homepage')
  


  return render(request,'vagas/details.html',{
    'vaga': vaga
  })

def criar_vaga(request):

  if not request.user.is_authenticated:
    messages.add_message(request,messages.INFO, 'Você precisa estar autenticado para criar uma vaga')
    return redirect('login')

  if request.method == 'GET':
    return render(request,'vagas/create-vaga.html')

  foto = request.POST.get('picture__input')
  print(foto)
  titulo =request.POST.get('nome-vaga')
  salario =request.POST.get('salario')
  localidade =request.POST.get('localidade')
  descricao_vaga =request.POST.get('desc-vaga')
  criador = request.user

  nova_vaga = Vaga(
    titulo_vaga     = titulo,
    descricao_vaga  = descricao_vaga,
    foto_vaga       = foto,
    salario_vaga    = salario,
    localidade_Vaga = localidade,
    owner = criador
  )
  nova_vaga.save()

  return render(request,'vagas/create-vaga.html')