from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from collections import defaultdict

# Create your views here.

"""
def index(request):
    imagen_us  = User.objects.get(id = 10)
    return render(request, 'index.html', { "usuario" : imagen_us.profile_picture.url })
"""
@login_required()
def index(request): 
     if request.method == "GET":
        # TRAER SALAS DEL USUARIO ACTUALEMTE AUTENTICADO
        salas = request.user.room_joined.all()  
        print(f"mis salas :{salas} ")
        return render(request, "index.html", {"salas": salas})
     else:
        # FORM + PARA AGRAGAR SALA: QUE LLAMA A CREAR SALA 
        return HttpResponseRedirect(reverse("crear_sala"))
     
@login_required()
def crear_sala(request): 
    if request.method == "POST": 
        nombre = request.POST.get("nombre_sala")
        descri = request.POST.get("descri_sala")
        date = request.POST.get("date_final")
        personas = request.POST.get("selected_users")
        personasLIST = personas.split(",")
        print("----------------------------------------------uuuuuuuuuuuuuuuu")
        print(personasLIST)
        if nombre and descri and date:
            #BBBBBB{print("llllllllllllllllllllllllllllllllllllllll")
            print(nombre)
            sala = Sala.objects.create(name=nombre, descripcion = descri, fechaf = date)
            sala.user.add(request.user) 
            
            for i in personasLIST: 
                # print(User.objects.filter(email= i))
                j = User.objects.filter(email= i)[0]
              
                print(f"id: {j.id} nombtr : {j.email}")
                sala.user.add(User.objects.filter(email= j.email)[0])
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "crear_sala.html", {"message": "El nombre de la sala no puede estar vacío."})
    
    # mandar a mostar una lista de los usuarios ps me pico la raja
    
    usuarios = User.objects.all().order_by('first_name', 'last_name')
    usuarios_por_inicial = defaultdict(list)
    for i in usuarios:
        first_name = i.first_name or "Sin nombre"
        inicial = first_name[0].upper()
        # guardar usuario en la jashteibol juelagramputa 
        datos_usuario = [f"{i.first_name} {i.last_name}", i.email]
        usuarios_por_inicial[inicial].append(datos_usuario) 
    usuarios_por_inicial = dict(usuarios_por_inicial)
    actual = request.user.email
    print(f"email de usuario actual : {actual}")
    print(usuarios_por_inicial)
    return render(request, "crear_sala.html", {'usuarios_ordenado': usuarios_por_inicial, "actual": actual})
    
# def salas(request, sala_id): 
# # TRAER LOS uers QUE ESTAN EN ESA SALA SELECCIONADA

def canvas(request):
    return render(request, "canvas.html")

@login_required()
def mostrar_sala(request, id_sala):
        sala = Sala.objects.filter(id = id_sala)
        
        print(f"adentro de: {sala}")
        print("uuuuuuuuuuuuuuuuuuuuuuuuuuu")
        print(sala[0].progreso())
        return render(request, "mi_sala.html", {"sala": sala[0]})  
    

def editar_fechai(request):
    if request.method =="POST":
        date = request.POST.get("date_final")
        id_sala = request.POST.get("id_sala")
        Sala.objects.filter(id=id_sala).update(fechai=date)
        sala = Sala.objects.filter(id = id_sala)
        return render(request, "mi_sala.html", {"sala": sala[0]})  

  
def register(request):
    if request.method == "POST":
        nombre = request.POST["username"]
        apellido = request.POST["apellidos"]
        password = request.POST["password"]
        confirmacion = request.POST["confirmation"]
        gmail = request.POST["gmail"]
        img = request.FILES.get("fotoo")  

        if password != confirmacion:
            return render(request, "register.html", {"message": "Las contraseñas no coinciden."})

        if User.objects.filter(email=gmail).exists():
            return render(request, "register.html", {"message": "Dirección de correo en uso."})

        try:
            # Crear el usuario
            usuario = User.objects.create(
                # PARA AUTENTICAR "CON GMAIL" USAR EL CAMPO USERNAME LUEG
                username=gmail,  
                email=gmail,
                first_name=nombre,
                last_name=apellido,
                password=make_password(password),
                profile_picture=img,
            )
        except IntegrityError:
            return render(request, "register.html", {"message": "Error al crear el usuario."})

        # LOGUEA A L USUARIO ;?
        login(request, user=usuario)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["gmail"]
        password = request.POST["password"]
        # jejej
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"message": "Correo o contraseña inválidos."})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))