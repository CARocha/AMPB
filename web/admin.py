from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]

class Emprendimientos_Inline(admin.TabularInline):
	model = Emprendimientos
	extra = 1

class EscuelaAdmin(admin.ModelAdmin):
	inlines = [Emprendimientos_Inline,]


class FotosEmprendimientos_Inline(admin.TabularInline):
	model = FotosEmprendimientos
	extra = 1

class EmprendimientosAdmin(admin.ModelAdmin):
	inlines = [FotosEmprendimientos_Inline,]

admin.site.register(Escuela)
admin.site.register(Emprendimientos,EmprendimientosAdmin)
admin.site.register(Banner)
admin.site.register(Actualidad)
admin.site.register(Evento)
admin.site.register(Liderazgo)
#admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Biblioteca)
admin.site.register(TipoRecurso)
# admin.site.register(Fases)
admin.site.register(ExperienciaLiderazgo)

#flatpages
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
#
# from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
# from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
#
# from django import forms
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
#
# class FlatpageForm(FlatpageFormOld):
#     content = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = FlatPage
#         fields = '__all__'
#
#
# class FlatPageAdmin(FlatPageAdminOld):
#     form = FlatpageForm

# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)
