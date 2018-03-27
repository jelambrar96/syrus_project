from django.http import HttpResponse
import datetime

def Hola(request):
    return HttpResponse("HolaMundo")

def Datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Date</h1><h3>%s</h3></body></html>" %now
    return HttpResponse(html)
