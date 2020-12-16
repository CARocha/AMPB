# -*- coding: utf-8 -*-
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from .models import *
from django.forms import Textarea
from django import forms

class InlineContenidos(NestedStackedInline):
    model = Contenidos
    extra = 1
    fk_name = 'modulo'
    can_delete = True

from datetime import datetime
class TemasModulos(NestedModelAdmin):
    inlines = [InlineContenidos]
    list_display = ('titulo', 'curso')
    search_fields = ('titulo',)
    list_filter = ('curso',)

    def save_model(self, request, obj, form, change):
        id_curso = obj.curso.id
        obj.save()
        #save fecha curso
        now = datetime.now()
        curso = Cursos.objects.get(id = id_curso)
        curso.fecha = now
        curso.save()

    def save_formset(self, request, form, formset, change):
        if change == True:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()

            #save fecha curso
            id_modulo = form.instance.id
            now = datetime.now()
            curso = Cursos.objects.get(modulos = id_modulo)
            curso.fecha = now
            curso.save()
        else:
            formset.save()


class CursosAdmin(NestedModelAdmin):
    list_display = ('titulo','fecha',)
    list_filter = ('fecha',)

# Register your models here.
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Modulos, TemasModulos)

class ReflexionForm(forms.ModelForm):
  class Meta:
    model = Reflexion
    widgets = {
      'texto': Textarea(attrs={'rows': 1,'cols': 40,'style': 'height: 100px;resize:none;',}),
    }
    fields = '__all__'

class ReflexionAdmin(admin.ModelAdmin):
    list_display = ('texto','fecha_creacion')
    form = ReflexionForm

admin.site.register(Reflexion, ReflexionAdmin)
