from django.urls import path
from .views import Artigo_1View, Artigo_2View, ArtigosView, ContatoView, Envio_artigosView, FerramentasView, IndexView, Mapa_siteView, ModeloView, NoticiasView, Politica_direitos_autoraisView, PublicidadeView, SobreView, Sofhie_sistemas_educacionaisView

urlpatterns = [
    
    path('artigo_1/',Artigo_1View.as_view(),name='artigo_1'),
    path('artigo_2/',Artigo_2View.as_view(),name='artigo_2'),
    path('artigos/',ArtigosView.as_view(),name='artigos'),
    path('contato/',ContatoView.as_view(),name='contato'),
    path('envio_artigos/',Envio_artigosView.as_view(),name='envio_artigos'),
    path('ferramentas/',FerramentasView.as_view(),name='ferramentas'),    
    path('',IndexView.as_view(),name='inicio'),
    path('mapa_site/',Mapa_siteView.as_view(),name='mapa_site'), 
    path('modelo/',ModeloView.as_view(),name='modelo'),
    path('noticias/',NoticiasView.as_view(),name='noticias'),
    path('politica_direitos_autorais/',Politica_direitos_autoraisView.as_view(),name='politica_direitos_autorais'),
    path('publicidade/',PublicidadeView.as_view(),name='publicidade'),
    path('sobre/',SobreView.as_view(),name='sobre'),
    path('sofhie_sistemas_educacionais/',Sofhie_sistemas_educacionaisView.as_view(),name='sofhie_sistemas_educacionais'),    
]

