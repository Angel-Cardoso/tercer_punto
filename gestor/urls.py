from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
	
	path('', views.inicio, name='inicio_view'),

	# Listas
	path('personal_list/', views.personal_list.as_view(), name='personal_list_view'),
	path('reuniones_list/', views.reuniones_list.as_view(), name='reuniones_list_view'),
	path('actividades_list/', views.actividades_list.as_view(), name='actividades_list_view'),
	path('proyectos_list/', views.proyectos_list.as_view(), name='proyectos_list_view'),
	path('clientes_list/', views.clientes_list.as_view(), name=' clientes_list_view'),
	path('avances_list/', views.avances_list.as_view(), name='avances_list_view'),
	path('pruebas/<str:slug>', views.pruebas.as_view(), name = 'pruebas_list_view'),
	# Detalles
	path('detalle_avance/<int:pk>', views.detalle_avance.as_view(), name = 'detalle_avance_view'),
	path('detalle_personal/<nombre_personal>', views.detalle_personal.as_view(), name = 'detalle_personal_view'),
	path('detalle_actividad/<int:pk>',views.detalle_actividad.as_view(), name = 'detalle_actividad_view'),
	path('detalle_proyecto/<int:pk>', views.detalle_proyecto.as_view(), name = 'detalle_proyecto_view'),
]