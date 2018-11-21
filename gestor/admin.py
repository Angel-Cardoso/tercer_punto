from django.contrib import admin

# Register your models here.
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

admin.site.register(Estados)
admin.site.register(Cargos)
admin.site.register(Sexos)
admin.site.register(Empresas)
admin.site.register(Proyectos)
admin.site.register(Personal)
admin.site.register(Proyecto_Empleado)
admin.site.register(Proyecto_Lider)
admin.site.register(Avances)
admin.site.register(Actividades)
admin.site.register(Actividad_Personal)
admin.site.register(Reuniones)
admin.site.register(Clientes)
admin.site.register(Reunion_Cliente)
admin.site.register(Reunion_Personal)