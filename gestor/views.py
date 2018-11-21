from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from .models import Estados
from .models import Cargos
from .models import Sexos
from .models import Empresas
from .models import Proyectos
from .models import Personal
from .models import Proyecto_Empleado
from .models import Proyecto_Lider		
from .models import Avances
from .models import Actividades
from .models import Actividad_Personal	
from .models import Reuniones
from .models import Clientes
from .models import Reunion_Cliente
from .models import Reunion_Personal
# Create your views here.

def inicio(request):
	return render(request, "gestor/inicio.html")

# Listas
class personal_list(generic.ListView):
	template_name = "gestor/personal.html"
	queryset = Personal.objects.all()

class proyectos_list(generic.ListView):
	template_name = "gestor/proyectos.html"
	queryset = Proyectos.objects.all()

class actividades_list(generic.ListView):
	template_name = "gestor/actividades.html"
	queryset = Actividades.objects.order_by('fecha_entrega')

class avances_list(generic.ListView):
	template_name = "gestor/avances.html"
	queryset = Avances.objects.all()

class clientes_list(generic.ListView):
	template_name = "gestor/clientes.html"
	queryset = Clientes.objects.all()

class reuniones_list(generic.ListView):
	template_name = "gestor/reuniones.html"
	queryset = Reuniones.objects.all()

# Detalles

class detalle_proyecto(generic.DetailView):
 	template_name = "gestor/detalle_proyecto.html"
 	model = Proyectos

class detalle_avance(generic.DetailView):
 	template_name = "gestor/detalle_avance.html"
 	model = Avances

class detalle_actividad(generic.DetailView):
 	template_name = "gestor/detalle_actividad.html"
 	model = Actividades

class detalle_personal(generic.DetailView):
 	template_name = "gestor/detalle_personal.html"
 	model = Personal

 	def get_object(self):
 		return get_object_or_404(Personal, nombre_personal__iexact=self.kwargs.get("nombre_personal"))

class pruebas(generic.DetailView):
 	template_name = "gestor/pruebas.html"
 	model = Proyectos

# def detalle_proyecto(request, id=1):
# 	proyecto = Proyectos.objects.get(id=id)
# 	contexto = {
# 	"proyecto" : proyecto
# 	}
# 	return render(request, "gestor/detalle_proyecto.html", contexto)