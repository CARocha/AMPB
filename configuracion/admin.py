from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import *

# Register your models here.
admin.site.register(Introduccion, SingletonModelAdmin)

class QuienesSomosAdmin(admin.ModelAdmin):
    list_display = ('titulo','orden')

admin.site.register(QuienesSomos,QuienesSomosAdmin)
