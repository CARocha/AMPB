from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import *

# Register your models here.
admin.site.register(Introduccion, SingletonModelAdmin)
admin.site.register(QuienesSomos)
