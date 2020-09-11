from django.db import models
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from lugar.models import *
# from django.contrib.gis.db import models as geo_models
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField
from location_field.models.plain import PlainLocationField

# Create your models here.
class Escuela(models.Model):
	nombre = models.CharField(max_length=300)
	foto = ImageField(upload_to='escuelas/')
	descripcion = RichTextUploadingField()
	pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
	departamento = ChainedForeignKey(Departamento,
					chained_field="pais",
					chained_model_field="pais")
	municipio = ChainedForeignKey(Municipio,
					chained_field="departamento",
					chained_model_field="departamento")
	lugar = models.CharField(max_length=250)
	location = PlainLocationField(based_fields=['lugar'], zoom=7)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Escuela, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Escuelas"

class Banner(models.Model):
	titulo = models.CharField(max_length=250)
	texto = models.TextField()
	foto = ImageField(upload_to='banner/')
	link = models.URLField()

	class Meta:
		verbose_name_plural = "Banners"

	def __str__(self):
		return self.titulo

class Actualidad(models.Model):
	titulo = models.CharField(max_length=250)
	fecha = models.DateField()
	contenido = RichTextUploadingField()
	foto = ImageField(upload_to='actualidad/',null=True,blank=True)
	video = EmbedVideoField(null=True,blank=True)
	escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	slug = models.SlugField(max_length=300,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Actualidad, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Actualidad"

	def __str__(self):
		return self.titulo

class Evento(models.Model):
	titulo = models.CharField(max_length=300)
	foto = ImageField(upload_to='eventos/')
	descripcion = RichTextUploadingField()
	inicio = models.DateField('Fecha de Inicio')
	fin = models.DateField('Fecha de Finalización',null=True, blank=True)
	hora_inicio = models.TimeField('Hora inicio')
	hora_fin = models.TimeField('Hora fin')
	lugar = models.CharField(max_length=250)
	location = PlainLocationField(based_fields=['lugar'], zoom=7)
	escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	slug = models.SlugField(max_length=300,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Evento, self).save(*args, **kwargs)

	def __str__(self):
		return self.titulo

class Liderazgo(models.Model):
	nombre = models.CharField(max_length=300)
	texto = models.TextField()
	foto = ImageField(upload_to='liderazgo/')
	escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.nombre

class Galeria(models.Model):
	nombre = models.CharField(max_length=300)
	foto = ImageField(upload_to='galeria/')
	escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	slug = models.SlugField(max_length=300,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Galeria, self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre

class Imagenes(models.Model):
	galeria = models.ForeignKey(Galeria,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=300)
	foto = ImageField(upload_to='galeria/imagenes/')

	class Meta:
		verbose_name_plural = "Imagenes"

class Biblioteca(models.Model):
	nombre = models.CharField(max_length=300)
	descripcion = RichTextUploadingField()
	foto = ImageField(upload_to='biblioteca/')
	archivo = models.FileField(upload_to='documentos-biblioteca/')
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	slug = models.SlugField(max_length=300,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Biblioteca, self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Biblioteca"