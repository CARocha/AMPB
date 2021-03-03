from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class TipoOrganizacion(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(TipoOrganizacion, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Tipos de organización"
		verbose_name = "Tipo de organización"

class AreaTrabajo(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(AreaTrabajo, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Áreas de trabajo"
		verbose_name = "Área de trabajo"

class Talleres(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Talleres, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Talleres"
		verbose_name = "Taller"

class TipoEmprendimiento(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(TipoEmprendimiento, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Tipos de Emprendimientos"
		verbose_name = "Tipo de Emprendimiento"

class Cargo(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Cargo, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Cargos"
		verbose_name = "Cargo"

CHOICES_RESIDE = ((1,'Dentro'),(2,'Fuera'))

ESCOLARIDAD_CHOICES = ((1,'Primaria incompleta'),(2,'Primaria completa'),
						(3,'Secundaria incompleta'),(4,'Secundaria completa'),
						(5,'Universidad incompleta'),(6,'Universidad completa'))

TRABAJO_CHOICES = ((1,'Medio tiempo'),(2,'Tiempo completo'),(3,'Por proyectos'),(4,'No trabaja'))

SEXO_CHOICES = ((1,'Mujer'),(2,'Hombre'),(3,'Otros'))

class Participantes(models.Model):
	nombre = models.CharField(max_length=250)
	edad = models.IntegerField()
	sexo = models.IntegerField(choices=SEXO_CHOICES)
	procedencia = models.CharField(max_length=250,verbose_name='Lugar de procedencia')
	reside = models.IntegerField(verbose_name='Reside dentro o fuera de la comunidad',choices=CHOICES_RESIDE)
	nivel_escolaridad = models.IntegerField(verbose_name='Nivel de escolaridad',choices=ESCOLARIDAD_CHOICES)
	trabajo = models.IntegerField(choices=TRABAJO_CHOICES)
	organizacion = models.ForeignKey('web.Escuela', verbose_name='Organización a la que pertenece', on_delete=models.CASCADE)
	cargo = models.ForeignKey(Cargo, verbose_name='Cargo en la organización', on_delete=models.CASCADE)
	fecha = models.DateField(verbose_name='Fecha en la que se incorporó a la Escuela')
	talleres = models.ManyToManyField(Talleres, verbose_name='Talleres de la Escuela en los que ha participado')

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Participantes"
		verbose_name = "Participante"