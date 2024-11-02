from django.http import HttpResponse
from django.shortcuts import render
from home.models import Settings

# Create your views here.

def index(request):
    settings = Settings.objects.first()
    print(settings)
#     birinci = "hepinize"
    metin = "BTK Kursiyerleri"
#   return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    context = {"sayfa":"home",
               'settings':settings}
    return render(request,'index.html',context)

def contact(request):
    settings = Settings.objects.first()
    print(settings)
#     birinci = "hepinize"
    metin = "BTK Kursiyerleri"
#   return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    context = {"sayfa":"Contact -Iletisim",
               'settings':settings}
    return render(request,'contact.html',context)