from configuracion.models import QuienesSomos

def globales(request):
    quienes_somos = QuienesSomos.objects.order_by('orden')
    return {'quienes_somos' : quienes_somos}
