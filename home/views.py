from django.http import HttpResponse
from django.shortcuts import render
from home.models import Settings

# Create your views here.

def index(request):
    settings = Settings.objects.get(pk=1)
#   birinci = "hepinize"
    metin = "BTK Kursiyerleri"
#   return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    context = {"sayfa": "home",
               'settings': settings}
    return render(request,'index.html',context)



def contact(request):
    settings = Settings.objects.get(pk=1)

    metin = "BTK Kursiyerleri"
#   return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    context = {"sayfa": "Contact -Iletisim",
               'settings': settings}
    return render(request,'contact.html',context)


def aboutus(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    context = {"sayfa": "About Us - Hakkımızda",
               'settings': settings}
    return render(request, 'references.html', context)


def references(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    context = {"sayfa": "References - Referanslar",
               'settings': settings}
    return render(request, 'references.html', context)