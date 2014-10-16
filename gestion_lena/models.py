# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

TIPO_TELEFONO = (
		(0, 'Movil'),
		(1, 'Fijo'),
		(2, 'No Menciona'),
	)

class Contacto(models.Model):
	'''
	Representa un Cliente que realiza 
	un pedido de leña.

	'''
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	tipo_telefono = models.IntegerField(choices=TIPO_TELEFONO, default=2)
	telefono = models.IntegerField(null=True,blank=True)
	direccion =	models.CharField(max_length=255)
	correo =  models.EmailField(null=True, blank=True)
	feha_de_registro = models.DateTimeField(auto_now_add=True)
	ultima_modificacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u"%s, %s" % (self.nombre, self.apellido)

	def get_absolute_url(self):
		return reverse('contacto_detail', kwargs={'pk': self.pk})

	def obtener_tipo_telefono(self):
		return TIPO_TELEFONO[self.tipo_telefono][1]

ESTADO_PEDIDO = (
	('En Proceso', 'En Proceso'),
	('Entregado', 'Entregado'),
	)


class Pedido(models.Model):
	'''
	Representa el pedido de leña que realiza un contacto.
	
	'''
	contacto = models.ForeignKey('Contacto')
	cantidad = models.PositiveIntegerField()
	direccion_destino = models.CharField(max_length=255) ## Cuidado
	estado = models.CharField(max_length=100, choices=ESTADO_PEDIDO, default="En Proceso")
	fecha_entrega = models.DateTimeField(null=True, blank=True)
	creado_en = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u"%s, %s" % (self.contacto, self.estado)

	def get_absolute_url(self):
		return reverse('pedido_detail', kwargs={'pk': self.pk})


class Ingreso(models.Model):
	pedido = models.OneToOneField("Pedido")
	valor = models.IntegerField()
	creado_en = models.DateTimeField(auto_now_add=True)


class TipoGasto(models.Model):
	nombre = models.CharField(max_length=255)
	creado_en = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Gasto(models.Model):
	tipo_gasto = models.ForeignKey("TipoGasto")
	valor = models.IntegerField()
	creado_en = models.DateTimeField(auto_now_add=True)


