# -*- coding: utf-8 -*-
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from .models import Cursos, Modulos, Contenidos

class InlineContenidos(NestedStackedInline):
    model = Contenidos
    extra = 1
    fk_name = 'modulo'
    can_delete = True

class TemasModulos(NestedModelAdmin):
    inlines = [InlineContenidos]
    list_display = ('titulo', 'curso')
    search_fields = ('titulo',)
    list_filter = ('curso',)

class CursosAdmin(NestedModelAdmin):
    list_display = ('titulo','fecha',)
    list_filter = ('fecha',)

# Register your models here.
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Modulos, TemasModulos)
