from django.http import HttpResponse
import datetime

def Hola(request):
    return HttpResponse("HolaMundo")

def Datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Date</h1><h3>%s</h3></body></html>" %now
    return HttpResponse(html)

def Hours_before(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body><h1>En %s Hora(s) seran: </h1><h3>%s</h3></body></html>" %(offset,dt)
    return HttpResponse(html)
