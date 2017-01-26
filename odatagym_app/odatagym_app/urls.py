"""odatagym_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from datasets_handler.views import DatasetsHandler
import examples.views as ex_views

from odatagym_app import settings

urlpatterns = [
    url(r'api/datasets/(?P<dataset_folder>[\w]+)/(?P<dataset_name>[\w-]+)/$',
        DatasetsHandler.as_view({'get': 'get'})),

    url(r'examples/sardinia_svg/', ex_views.get_sardinia_svg_example),
    url(r'examples/bandalarga/', ex_views.get_banda_larga),
    url(r'examples/veicolirimossi/', ex_views.get_veicoli_rimossi),
    url(r'examples/postiletto/', ex_views.get_posti_letto),
    url(r'examples/postiletto2010/', ex_views.get_posti_letto_2010),
    url(r'examples/bandalarga2015/', ex_views.get_banda_larga_2015),
    url(r'examples/bandalarga2018/', ex_views.get_banda_larga_2018),
    url(r'examples/bandalarga2020/', ex_views.get_banda_larga_2020),
    url(r'examples/sardinia_drugstores/', ex_views.get_sardinia_drugstores),
    url(r'examples/rome_accidents/', ex_views.get_rome_accidents),

    url(r'^admin/', include(admin.site.urls)),
]
