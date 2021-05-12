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
from monitoreo.models import *

# Create your models here.
# class Fases(models.Model):
# 	nombre = models.CharField(max_length=300)
# 	descripcion = RichTextUploadingField()

# 	def __str__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Fases"
# 		verbose_name = "Fase"

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
	fundacion = models.DateField()
	tipo_organizacion = models.ForeignKey(TipoOrganizacion, verbose_name="Tipo de organización", on_delete=models.CASCADE,null=True,blank=True)
	area_trabajo = models.ManyToManyField(AreaTrabajo, verbose_name="Área de trabajo",blank=True)
	nombre_referencia = models.CharField(max_length=300,null=True,blank=True)
	cargo_referencia = models.CharField(max_length=300,null=True,blank=True)
	telefono_referencia = models.CharField(max_length=300,null=True,blank=True)
	correo_referencia = models.EmailField( max_length=300,null=True,blank=True)
	hombres = models.IntegerField(default=0)
	mujeres = models.IntegerField(default=0)
	otros = models.IntegerField(default=0)
	talleres_impartidos = models.ManyToManyField(Talleres,blank=True)
	# fase = models.ForeignKey(Fases,on_delete=models.CASCADE,blank=True,null=True)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Escuela, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Núcleos"
		verbose_name = "Núcleo"

class Emprendimientos(models.Model):
	escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE,verbose_name='Núcleo')
	titulo = models.CharField(max_length=300)
	tipo = models.ForeignKey(TipoEmprendimiento,on_delete=models.CASCADE,null=True,blank=True)
	descripcion = models.TextField()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Emprendimientos"

class FotosEmprendimientos(models.Model):
	emprendimientos = models.ForeignKey(Emprendimientos, on_delete=models.CASCADE)
	foto = ImageField(upload_to='emprendimientos/')

	class Meta:
		verbose_name_plural = "Fotos"
		verbose_name = "Foto"

class Banner(models.Model):
	titulo = models.CharField(max_length=250)
	texto = models.TextField()
	foto = ImageField(upload_to='banner/')
	link = models.URLField(blank=True,null=True)

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
		verbose_name_plural = "Noticias"
		verbose_name = "noticia"

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

class TipoRecurso(models.Model):
	nombre = models.CharField(max_length=300)

	def __str__(self):
		return self.nombre

class Biblioteca(models.Model):
	nombre = models.CharField(max_length=300)
	descripcion = models.TextField()
	foto = ImageField(upload_to='biblioteca/')
	archivo = models.FileField(upload_to='documentos-biblioteca/')
	fecha = models.DateField()
	tipo = models.ForeignKey(TipoRecurso,on_delete=models.CASCADE,null=True,blank=True)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	slug = models.SlugField(max_length=300,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Biblioteca, self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Recursos"
		verbose_name = "recurso"

class ExperienciaLiderazgo(models.Model):
	titulo = models.CharField(max_length=250)
	fecha = models.DateField()
	contenido = RichTextUploadingField()
	foto = ImageField(upload_to='actualidad/',null=True,blank=True)
	video = EmbedVideoField(null=True,blank=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	slug = models.SlugField(max_length=300,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(ExperienciaLiderazgo, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Experiencias de Liderazgo"
		verbose_name = "experiencia de liderazgo"

	def __str__(self):
		return self.titulo
