from django.contrib import admin
from .models import *
from nested_inline.admin import *
from django.db.models import Sum

# Register your models here.
admin.site.register(TipoOrganizacion)
admin.site.register(AreaTrabajo)
admin.site.register(Talleres)
admin.site.register(TipoEmprendimiento)
admin.site.register(Cargo)
admin.site.register(Participantes)
admin.site.register(Formadores)
admin.site.register(PerfilVocacional)

class Ejecucion_Inline(NestedTabularInline):
    model = Ejecucion
    extra = 1
    max_num = 12
 
class AnioEjecucion_Inline(NestedTabularInline):
    model = AnioEjecucion
    extra = 1
    inlines = [Ejecucion_Inline,]

class Presupuesto_Inline(NestedTabularInline):
    model = Presupuesto
    inlines = [AnioEjecucion_Inline,]
    extra = 1
    readonly_fields = ['saldo',]

class HomologacionFondosAdmin(NestedModelAdmin):
    inlines = [Presupuesto_Inline,]

    def add_view(self, request, form_url='', extra_context=None):
        self.readonly_fields = ''
        return super(HomologacionFondosAdmin, self).add_view(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ('rubro',)
        return super(HomologacionFondosAdmin, self).change_view(request,object_id)
    

    def save_formset(self, request, form, formset, change):
        if formset.model == Presupuesto:
            presupuesto = formset.save(commit=False)
            for pre in presupuesto:
                ejecucion_query = Ejecucion.objects.filter(anioejecucion__presupuesto = pre).aggregate(total = Sum('ejecucion'))['total'] or 0
                pre.saldo = pre.presupuesto - ejecucion_query
                pre.save()

        if formset.model == Ejecucion:
            ejecucion = formset.save(commit=True)
            for ej in ejecucion:
                presupuesto = Presupuesto.objects.get(anioejecucion = ej.anioejecucion)
                ejecucion_query = Ejecucion.objects.filter(anioejecucion__presupuesto = presupuesto).aggregate(total = Sum('ejecucion'))['total'] or 0
                presupuesto.saldo = presupuesto.presupuesto - ej.ejecucion - ejecucion_query
                presupuesto.save()
                ej.save()
        return super(HomologacionFondosAdmin, self).save_formset(request, form, formset, change)

admin.site.register(HomologacionFondos,HomologacionFondosAdmin)

class Producto_Inline(admin.TabularInline):
    model = Producto
    extra = 1

class RubroAdmin(admin.ModelAdmin):
    inlines = [Producto_Inline,]

admin.site.register(Rubro,RubroAdmin)
admin.site.register(FuenteFinanciamiento)