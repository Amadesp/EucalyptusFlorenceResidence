from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# email
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText



# Create your views here.
from . models import *
#Email 
def Enviar_Email_Contact(request):
    # send_mail('Assunto','mensagem','amademelkisdek00@gmail.com',['tec.scorpion00@gmail.com']
    
    if request.method == 'POST':
        
        server = smtplib.SMTP(Emscorpionaiml['host.king.net'],Emscorpionaiml['465'])

        server.ehlo()
        server.starttls()
        server.login(Emscorpionaiml['cley@gmail.com'],Emscorpionaiml['0rhjddgsgdgs'])

        nome = request.POST.get('nome')
        email_to = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        mensagem_ = request.POST.get('mensagem')

        corpo = f'Nome : {nome} \nEmail : {email_to} \nTelefoe : {telefone}\nAssunto : {assunto}\n\n{mensagem_}'

        email_msg = MIMEMultipart()
        email_msg['From'] = email_to
        email_msg['To'] = Emscorpionaiml['cley@gmail.com']
        email_msg['Subject'] = f'{assunto}'
        email_msg.attach(MIMEText(corpo,'plain'))

        server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
        server.quit()
        return redirect('contacte-nos')

    else:
        return render(request,'contact.html')

def home(request):
    baner = Banner.objects.all().order_by('-id')
    data_servicos = DemoServicos.objects.all().order_by('-id')
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_contactos = Contactos.objects.all().order_by('-id')
    data_siga_nos = Siga.objects.all().order_by('-id')

    data_fotos = Fotos_all.objects.all().order_by('-id')
    data_fotos_exterior = Fotos_exterior_home.objects.all().order_by('-id')
    data_fotos_quartos = Fotos_quartos_home.objects.all().order_by('-id')
    data_fotos_restaurante = Fotos_restaurante_home.objects.all().order_by('-id')

    return render(request,'index.html',
    {
        'baner':baner,
        'data_servicos':data_servicos,
        'data_contactos':data_contactos,
        'data_siga_nos':data_siga_nos,
        'data_localizacao':data_localizacao,
        # fotos  
        'data_fotos':data_fotos,
        'data_fotos_exterior': data_fotos_exterior,
        'data_fotos_quartos':data_fotos_quartos,
        'data_fotos_restaurante':data_fotos_restaurante,

        
    }
    )


def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('_p')
            password2 = request.POST.get('__p')


            user = User.objects.filter(username=username).first()

            if user:
                messages.info(request,'Usuario já existe!')
            elif password1 != password2:
                messages.info(request,'Palavra passe diferente!')
            else:
                if password1 == password2:
                    user = User.objects.create_user(username=username,email=email,password=password1)
                    user.save()
                    return redirect('login')

        context = {}
        return render(request,'accounts/register.html',context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Senha ou nome do usuario invalido!')
        context = {}
        return render(request,'accounts/login.html',context)


def Logout(request):
    logout(request)
    return redirect('login')


def Quartos(request):
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_baner_quartos = Banner_quartos.objects.all().order_by('-id')

    data_fotos = Fotos_all_quartos.objects.all().order_by('-id')
    data_fotos_quartos = Fotos_quartos.objects.all().order_by('-id')
    data_fotos_outras = Fotos_outras_quartos.objects.all().order_by('-id')
    data_quarto_preco = Quartos_preco.objects.all().order_by('-id')


    return render(request, 'serv/plataforma-quartos.html',
    {
        'data_baner_quartos': data_baner_quartos,
        'data_localizacao': data_localizacao,
        
        'data_fotos':data_fotos,
        'data_fotos_quartos': data_fotos_quartos,
        'data_fotos_outras':data_fotos_outras,
        'data_quarto_preco':data_quarto_preco,
    }
    )


def Restaurante(request):
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_baner_restaurante = Banner_restaurante.objects.all().order_by('-id')

    data_fotos = Fotos_all_restaurante.objects.all().order_by('-id')
    data_fotos_restaurante = Fotos_restaurante.objects.all().order_by('-id')
    data_fotos_outras = Fotos_outras_restaurante.objects.all().order_by('-id')
    
    return render(request, 'serv/plataforma-restaurante.html',
    {
        'data_baner_restaurante':data_baner_restaurante,
        'data_localizacao': data_localizacao,

        'data_fotos':data_fotos,
        'data_fotos_restaurante': data_fotos_restaurante,
        'data_fotos_outras':data_fotos_outras,
    }
    )

@login_required(login_url='login')
def Jardim_infantil(request):
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_baner_jardim_infantil = Banner_jardim_infantil.objects.all().order_by('-id')
    data_fotos_jardim_infantil = Fotos_all_jardim_infantil.objects.all().order_by('-id')

    return render(request, 'serv/plataforma-jardim-infantil.html',
    {
        'data_baner_jardim_infantil': data_baner_jardim_infantil,
        'data_baner_jardim_infantil': data_fotos_jardim_infantil,
        'data_localizacao': data_localizacao,
    }
    )
@login_required(login_url='login')
def Piscina(request):
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_baner_piscina = Banner_piscina.objects.all().order_by('-id')
    data_fotos_piscina = Fotos_all_piscina.objects.all().order_by('-id')

    return render(request, 'serv/plataforma-piscina.html',
    {
        'data_baner_piscina': data_baner_piscina,
        'data_fotos_piscina': data_fotos_piscina,
        'data_localizacao': data_localizacao,
    }
    )

@login_required(login_url='login')
def Auditorio(request):
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_baner_aud = Banner_auditorio.objects.all().order_by('-id')
    data_fotos_aud = Fotos_all_auditorio.objects.all().order_by('-id')

    return render(request, 'serv/plataforma-auditorio.html',
    {
        'data_baner_aud': data_baner_aud,
        'data_fotos_aud': data_fotos_aud,
        'data_localizacao': data_localizacao,
    }
    )

@login_required(login_url='login')
def Jardim(request):
    data_localizacao = Localizacao_mapa.objects.all().order_by('-id')
    data_baner_jardim = Banner_jardim.objects.all().order_by('-id')
    data_fotos_jardim = Fotos_all_jardim.objects.all().order_by('-id')

    return render(request, 'serv/plataforma-jardim.html',
    {
        'data_baner_jardim': data_baner_jardim,
        'data_baner_jardim': data_fotos_jardim,
        'data_localizacao': data_localizacao,
    }
    )

