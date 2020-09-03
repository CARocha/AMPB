from .models import Cursos, Modulos, Contenidos
from rest_framework import serializers

class CursoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cursos
		fields = ('id','titulo','imagen','imagen_banner','descripcion','fecha')

class ModulosSerializer(serializers.ModelSerializer):
	# curso = CursoSerializer()

	class Meta:
		model = Modulos
		fields = ('id', 'curso', 'titulo', 'order')

class ContenidoSerializer(serializers.ModelSerializer):
	# modulo = ModulosSerializer()

	class Meta:
		model = Contenidos
		fields = ('id','modulo','titulo','contenido','order','url_video','nombre_video')