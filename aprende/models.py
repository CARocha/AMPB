# -*- coding: utf-8 -*-
from django.db import models
from django.db import models
from .fields import OrderField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField,get_thumbnail

# Create your models here.

class Cursos(models.Model):
	titulo = models.CharField('Nombre del curso', max_length=250)
	slug = models.SlugField(max_length=250, unique=True, editable=False)
	imagen = ImageField(upload_to='images', null=True, blank=True)
	#imagen_banner = models.FileField(upload_to='banner', null=True, blank=True)
	descripcion = RichTextUploadingField('Descripción del curso')
	fecha = models.DateTimeField(auto_now=True,verbose_name='Ultima actualización')
	activo = models.BooleanField(default=True)

	class Meta:
		ordering = ('-fecha',)
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = (slugify(self.titulo))
		super(Cursos, self).save(*args, **kwargs)
	
	@property
	def cached_img(self):
		im = get_thumbnail(self.imagen, '1000', crop='center', quality=99)
		return im.url


class Modulos(models.Model):
	curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
	titulo = models.CharField('Nombre del tema', max_length=250)
	order = OrderField(blank=True, for_fields=['curso'])

	class Meta:
		ordering = ['order']
		verbose_name = 'Tema'
		verbose_name_plural = 'Temas'

	def __str__(self):
		return '{0}. {1}'.format(self.order, self.titulo)

class Contenidos(models.Model):
	modulo = models.ForeignKey(Modulos,on_delete=models.CASCADE)
	titulo = models.CharField('Nombre de la lección', max_length=250)
	contenido = RichTextUploadingField('Contenido de la lección')
	order = OrderField(blank=True, for_fields=['modulo'])
	url_video = models.URLField(null = True, blank = True)
	nombre_video = models.CharField('Nombre del video', max_length=250,
									null=True, blank=True)

	class Meta:
		ordering = ['order']
		verbose_name = 'Lección'
		verbose_name_plural = 'Lecciones'

	def __str__(self):
		return self.titulo