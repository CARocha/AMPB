from .models import *
from rest_framework import serializers

SEARCH_PATTERN = 'src=\"/media/uploads/'
SITE_DOMAIN = "http://www.escuelamesoamericana.org"
REPLACE_WITH = 'src=\"%s/media/uploads/' % SITE_DOMAIN

class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text

class CursoSerializer(serializers.ModelSerializer):
	imagen = serializers.CharField(source='cached_img')
	class Meta:
		model = Cursos
		fields = ('id','titulo','imagen','descripcion','fecha','activo')

class ModulosSerializer(serializers.ModelSerializer):
	# curso = CursoSerializer()
	orden = serializers.IntegerField(source='order')

	class Meta:
		model = Modulos
		fields = ('id', 'curso', 'titulo', 'orden')

class ContenidoSerializer(serializers.ModelSerializer):
	# modulo = ModulosSerializer()
	contenido = FixAbsolutePathSerializer()
	orden = serializers.IntegerField(source='order')

	class Meta:
		model = Contenidos
		fields = ('id','modulo','titulo','contenido','orden','url_video','nombre_video')

class ReflexionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reflexion
		fields = ('id','texto','autor','link','activo','fecha_creacion')
