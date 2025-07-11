
def home(request):
    return render(request, 'index.html')

from django.shortcuts import render

def inicio(request):
    return render(request, "sitebrba/inicio.html")

elenco_brba = [
    {"nome": "Walter", "Idade (em serie)": 32, "personagem:" "vilão", "img:" "walter"},
]

def elencobrba(request):
        context = {
              "elencobrba": elenco_brba,
        }
        return render(request, "sitebrba/elenco.html", context)

def sobre(request):
      return render(request, "sitebrba/sobre.html")