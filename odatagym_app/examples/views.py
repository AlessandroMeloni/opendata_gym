from django.shortcuts import render

from odatagym_app.settings import GOOGLE_API_KEY


def get_sardinia_svg_example(request):
    return render(request, 'sardinia_svg.html')


def get_banda_larga_2018(request):
    return render(request, 'bandalarga2018.html')

def get_banda_larga_2020(request):
    return render(request, 'bandalarga2020.html')


def get_banda_larga_2015(request):
    return render(request, 'bandalarga2015.html')

def get_banda_larga(request):
    return render(request, 'bandalarga.html')

def get_veicoli_rimossi(request):
    return render(request, 'veicolirimossi.html',
                  context={'google_api_key': GOOGLE_API_KEY})

def get_veicoli_rimossi_heatmap(request):
    return render(request, 'veicolirimossiheatmap.html',
                  context={'google_api_key': GOOGLE_API_KEY})

def get_posti_letto(request):
    return render(request, 'postiletto.html')

def get_posti_letto_2010(request):
    return render(request, 'postiletto2010.html')

def get_sardinia_drugstores(request):
    return render(request, 'markers.html',
                  context={'google_api_key': GOOGLE_API_KEY})

def get_rome_accidents(request):
    return render(request, 'heatmap.html',
                  context={'google_api_key': GOOGLE_API_KEY})
