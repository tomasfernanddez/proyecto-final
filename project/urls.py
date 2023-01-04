"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from ejemplo.views import (index, saludar_a, sumar, 
                            buscar, mostrar_familiares, 
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, 
                            FamiliarBorrar, FamiliarActualizar,
                            FamiliarDetalle, AutoList, AutoCrear, 
                            AutoBorrar, AutoActualizar,
                            AutoDetalle, MascotaList, MascotaCrear, 
                            MascotaBorrar, MascotaActualizar,
                            MascotaDetalle, BuscarMascota, BuscarAuto)
from ejemplo_dos.views import (index, PostListar, PostCrear, PostBorrar, 
                                PostActualizar, PostDetalle, UserSignUp,
                                UserLogin, UserLogout)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path("saludar-a/<nombre>/", saludar_a),
    path("sumar/<int:a>/<int:b>/", sumar),
    path("buscar/", buscar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('success_updated_message', TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-auto/', AutoList.as_view()),
    path('panel-auto/crear', AutoCrear.as_view()),
    path('panel-auto/<int:pk>/borrar', AutoBorrar.as_view()),
    path('panel-auto/<int:pk>/actualizar', AutoActualizar.as_view()),
    path('success_updated_message_auto', TemplateView.as_view(template_name="ejemplo/success_updated_message_auto.html")),
    path('panel-auto/<int:pk>/detalle', AutoDetalle.as_view()),
    path('panel-mascota/', MascotaList.as_view()),
    path('panel-mascota/crear', MascotaCrear.as_view()),
    path('panel-mascota/<int:pk>/borrar', MascotaBorrar.as_view()),
    path('panel-mascota/<int:pk>/actualizar', MascotaActualizar.as_view()),
    path('success_updated_message_mascota', TemplateView.as_view(template_name="ejemplo/success_updated_message_mascota.html")),
    path('panel-mascota/<int:pk>/detalle', MascotaDetalle.as_view()),
    path('panel-mascota/buscar', BuscarMascota.as_view()),
    path('panel-auto/buscar', BuscarAuto.as_view()),
    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/listar', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/<int:pk>/detalle', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/signup', UserSignUp.as_view(), name="ejemplo-dos-signup"),
    path('ejemplo-dos/login', UserLogin.as_view(), name="ejemplo-dos-login"),
    path('ejemplo-dos/logout', UserLogout.as_view(), name="ejemplo-dos-logout"),
]
