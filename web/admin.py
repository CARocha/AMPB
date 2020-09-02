from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]

admin.site.register(Escuela,LeafletGeoAdmin)
admin.site.register(Banner)
admin.site.register(Actualidad)
admin.site.register(Evento)
admin.site.register(Liderazgo)
admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Biblioteca)