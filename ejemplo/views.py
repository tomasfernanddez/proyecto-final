from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm, BuscarAuto, BuscarMascota
from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from ejemplo.models import Auto
from ejemplo.models import Mascota

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request, 
    "ejemplo/saludar_a.html",
    {"nombre": nombre}
    )


def sumar(request, a, b):
    return render (request, 
    "ejemplo/sumar.html", 
    {"a": a,
    "b": b,
    "resultado": a + b,
    }
    )


def buscar(request):
    lista_de_nombre = ["German", "Daniel", "Romero", "Alvaro"]
    query = request.GET["q"]
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = "no hay match"
    return render(request, "ejemplo/buscar.html", {"resultado": resultado})


def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "fecha":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "fecha":"", "numero_pasaporte":""}
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})


class FamiliarList(ListView):
  model = Familiar


class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "fecha", "numero_pasaporte"]


class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"


class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/success_updated_message"
  fields = ["nombre", "direccion", "fecha", "numero_pasaporte"]


class FamiliarDetalle(DetailView):
  model = Familiar
  fields = ["nombre", "direccion", "fecha", "numero_pasaporte"]

class AutoList(ListView):
  model = Auto

class AutoCrear(CreateView):
  model = Auto
  success_url = "/panel-auto"
  fields = ["marca", "modelo", "color", "patente"]

class AutoBorrar(DeleteView):
  model = Auto
  success_url = "/panel-auto"

class AutoActualizar(UpdateView):
  model = Auto
  success_url = "/success_updated_message_auto"
  fields = ["marca", "modelo", "color", "patente"]

class AutoDetalle(DetailView):
  model = Auto
  fields = ["marca", "modelo", "color", "patente"]


class MascotaList(ListView):
  model = Mascota

class MascotaCrear(CreateView):
  model = Mascota
  success_url = "/panel-mascota"
  fields = ["nombre", "animal", "raza", "fecha"]

class MascotaBorrar(DeleteView):
  model = Mascota
  success_url = "/panel-mascota"

class MascotaActualizar(UpdateView):
  model = Mascota
  success_url = "/success_updated_message_mascota"
  fields = ["nombre", "animal", "raza", "fecha"]

class MascotaDetalle(DetailView):
  model = Mascota
  fields = ["nombre", "animal", "raza", "fecha"]


class BuscarAuto(View):
    form_class = BuscarAuto
    template_name = 'ejemplo/auto_buscar.html'
    initial = {"marca":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            marca = form.cleaned_data.get("marca")
            object_list = Auto.objects.filter(marca__icontains=marca).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'object_list':object_list})
        return render(request, self.template_name, {"form": form})

class BuscarMascota(View):
    form_class = BuscarMascota
    template_name = 'ejemplo/mascota_buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            object_list = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'object_list':object_list})
        return render(request, self.template_name, {"form": form})