from django.http import HttpResponse

def Hola(request):
    return HttpResponse("HolaMundo")

