from django.contrib import admin
from .models import *
from nested_inline.admin import *

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
    extra = 1

class HomologacionFondosAdmin(NestedModelAdmin):
    inlines = [Presupuesto_Inline,AnioEjecucion_Inline]

admin.site.register(HomologacionFondos,HomologacionFondosAdmin)
admin.site.register(Rubro)
admin.site.register(FuenteFinanciamiento)