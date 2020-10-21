from .models import Cursos, Modulos, Contenidos
from rest_framework import serializers

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
	orden = serializers.IntegerField(source='order')

	class Meta:
		model = Contenidos
		fields = ('id','modulo','titulo','contenido','orden','url_video','nombre_video')
