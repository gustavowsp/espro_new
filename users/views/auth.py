from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import re

def info_exists(infos):
        """
        True: Foram enviadas
        False: Não foram enviadas

        Essa função retorna se todas as informações necessárias 
        foram enviadas.
        """

        for value in infos.values():
            
            if not value:
                return False
            else: 
                envite = True

        return envite


def login_view(request):

    if request.method == 'GET':
        return render(request,'users/login.html')
     
    # Pegando informações enviadas
    info = {
        'username'      :   request.POST.get('username').lower(),
        'password'      :   request.POST.get('password') ,
    }

    # Verificando se as informações foram enviadas
    if not info_exists(info):
        messages.add_message(request,messages.WARNING,'Você precisa preencher todos os campos')
        return render(request,'users/login.html')
    
    # Autenticando o usuário
    usuario_object = authenticate(
        username=info['username'],
        password=info['password']
    )
    
    # Se o usuário estiver correto vou loga-lo
    if usuario_object:
        login(request,usuario_object)
        return redirect('login')
    else:
        messages.add_message(request,messages.ERROR,'Esse usuário não existe, ou você errou sua senha.')
        
    return render(request,'users/login.html')

def register(request):
    
    def exists_user(infos):
        """
        Verifica se já existe um user com este username.
        True: Existe
        False: Não existe
        """
        try:
            User.objects.get(username=infos['username_get'])
            exists = True
        except:
            exists = False
        
        return exists

    def email_utilizing(infos):
        """
        Verifica se já existe um user com este email.
        True: Existe
        False: Não existe
        """

        try:
            User.objects.get(email=infos['email'])
            exists = True
        except:
            exists = False
        return exists

                         
    if request.method == 'POST':
        
        # Pegando informações enviadas
        user_info = {
        'username_get'      :   request.POST.get('username').lower(),
        'password_get'      :   request.POST.get('password') ,
        'first_name_get'    :   request.POST.get('first_name'),
        'email'     :   request.POST.get('email'),
        }

        # Validando se todas as informações foram enviadas
        if not info_exists(user_info):
            messages.add_message(request,messages.INFO, "Você precisa preencher todos os campos!")
            return render(request,'users/registerpage.html')
        
        if bool(re.search(r"\s", user_info['username_get'])):
            messages.add_message(request,messages.INFO, "O username não pode ter espaços")
            return render(request,'users/registerpage.html')
        
        # Verificando se esse usuário já existe
        if exists_user(user_info):
            messages.add_message(request,messages.INFO, "Este username já está sendo utilizado")
            return render(request,'users/registerpage.html')

        # Verificando se o email já está sendo utilizado
        if email_utilizing(user_info):
            messages.add_message(request,messages.INFO, "Este email já está sendo utilizado")
            return render(request,'users/registerpage.html')

        #Validando senhas

        # Se o usuário passou por tudo isso, sua conta será criada
        new_user = User.objects.create_user(
            username=user_info['username_get'],
            first_name=user_info['first_name_get'],
            email = user_info['email'],
            password = user_info['password_get']
        )
    
        messages.add_message(request,messages.SUCCESS,'Usuário criado')
        return redirect('login')
    return render(request,'users/registerpage.html')

def logout_view(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect('login')