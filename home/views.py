from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
#     birinci = "hepinize"
    metin = "BTK Kursiyerleri"
#     return HttpResponse("Hello,%s. <br> You are at the"% metin)
    #return HttpResponse(metin)
    context = {"icerik1":metin}
    return render(request,'index.html')
