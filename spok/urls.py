
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta para la vista 'index'
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('crear_sala/', views.crear_sala, name='crear_sala'),
    path('mostrar_sala/<int:id_sala>', views.mostrar_sala, name='mostrar_sala'),
    path('editar_fechai/', views.editar_fechai, name='editar_fechai'),
    path('canvas/', views.canvas, name='canvas')
]
