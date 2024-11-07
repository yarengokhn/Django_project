from django.http import HttpResponse
from django.shortcuts import render
from home.forms import ContactForm
from home.models import Settings

# Create your views here.

def index(request):
    settings = Settings.objects.first()
#   birinci = "hepinize"
    metin = "BTK Kursiyerleri"
#   return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    context = {"sayfa": "home",
               'settings': settings}
    return render(request,'index.html',context)



def contact(request):
    settings = Settings.objects.first()
    metin = "BTK Kursiyerleri"
#   return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    form = ContactForm()
    context = {"sayfa": "Contact -Iletisim",
               'settings': settings,
               'form': form}
    return render(request,'contact.html',context)


def aboutus(request):
    settings = Settings.objects.first()

    metin = "BTK Kursiyerleri"
    context = {"sayfa": "About Us - Hakkımızda",
               'settings': settings}
    return render(request, 'references.html', context)


def references(request):
    settings = Settings.objects.first()

    metin = "BTK Kursiyerleri"
    context = {"sayfa": "References - Referanslar",
               'settings': settings}
    return render(request, 'references.html', context)