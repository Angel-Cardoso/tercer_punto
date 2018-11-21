from django.db import models
# Create your models here.

class Estados(models.Model):
	estado = models.CharField(max_length = 20)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.estado)

class Cargos(models.Model):
	nombre_cargo = models. CharField(max_length = 20)
	descripcion = models.CharField(max_length = 100)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_cargo)

class Sexos(models.Model):
	sexo = models.CharField(max_length = 20)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.sexo)

class Empresas(models.Model):
	nombre_empresas = models.CharField(max_length = 40)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_empresas)

class Proyectos(models.Model):
	nombre_proyecto = models.CharField(max_length = 40)
	descripcion = models.CharField(max_length = 100)
	estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_proyecto)

class Personal(models.Model):
	nombre_personal = models.CharField(max_length = 40)
	edad = models.IntegerField()
	sexo = models.ForeignKey(Sexos, on_delete=models.CASCADE)
	telefono = models.IntegerField()
	cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_personal)

class Proyecto_Empleado(models.Model):
	nombre_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
	nombre_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_proyecto)

class Proyecto_Lider(models.Model):
	nombre_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
	nombre_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_proyecto)		

class Avances(models.Model):
	nombre_avance = models.CharField(max_length = 40)
	nombre_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length = 100)
	fecha_entrega = models.DateTimeField()
	estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_avance)

class Actividades(models.Model):
	nombre_avance = models.ForeignKey(Avances, on_delete=models.CASCADE)
	nombre_actividad = models.CharField(max_length = 40)
	descripcion = models.CharField(max_length = 100)
	fecha_entrega = models.DateTimeField()
	estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_actividad)

class Actividad_Personal(models.Model):
	nombre_actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)
	nombre_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_actividad)	

class Reuniones(models.Model):
	nombre_reunion = models.CharField(max_length = 40)
	nombre_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
	lugar = models.CharField(max_length = 100)
	descripcion = models.CharField(max_length = 100)
	fecha_reunion = models.DateTimeField()
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_reunion)

class Clientes(models.Model):
	nombre_cliente = models.CharField(max_length = 40)
	edad = models.IntegerField()
	sexo = models.ForeignKey(Sexos, on_delete=models.CASCADE)
	telefono = models.IntegerField()
	empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_cliente)

class Reunion_Cliente(models.Model):
	nombre_reunion = models.ForeignKey(Reuniones, on_delete=models.CASCADE)
	nombre_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_reunion)

class Reunion_Personal(models.Model):
	nombre_reunion = models.ForeignKey(Reuniones, on_delete=models.CASCADE)
	nombre_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_reunion)