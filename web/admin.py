from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]

admin.site.register(Escuela)
admin.site.register(Banner)
admin.site.register(Actualidad)
admin.site.register(Evento)
admin.site.register(Liderazgo)
#admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Biblioteca)

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
