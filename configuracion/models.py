from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms.fields import URLField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField
from solo.models import SingletonModel
from django.template.defaultfilters import slugify

# Create your models here.
class Introduccion(SingletonModel):
	titulo = models.CharField(max_length = 250)
	subtitulo = models.CharField(max_length = 250)
	texto = models.TextField()
	imagen = ImageField(upload_to='intro/',null=True,blank=True)
	video = EmbedVideoField(null=True,blank=True)
	link_facebook = models.URLField(null=True,blank=True)
	link_twitter = models.URLField(null=True,blank=True)
	link_instagram = models.URLField(null=True,blank=True)

	def __str__(self):
		return "Introducción"

	class Meta:
		verbose_name = "Introducción"

class QuienesSomos(models.Model):
	titulo = models.CharField(max_length = 250)
	texto = RichTextUploadingField()
	slug = models.SlugField(max_length=250,editable=False)
	orden = models.IntegerField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(QuienesSomos, self).save(*args, **kwargs)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Quienes Somos"

class Contectenos(SingletonModel):
	antes_de_contactarnos = models.TextField()
	# direccion = models.CharField(max_length = 250,null=True,blank=True)
	correo = models.URLField()
	# telefono = models.CharField(max_length = 250,null=True,blank=True)

	def __str__(self):
		return "Contáctenos"

	class Meta:
		verbose_name = "Contáctenos"
