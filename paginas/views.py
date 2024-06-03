from django.views.generic import TemplateView


# Create your views here.

class Artigo_1View(TemplateView):  # Artigo 1
    template_name = "artigo_1.html"

class Artigo_2View(TemplateView):  # Artigo 2
    template_name = "artigo_2.html"

class ArtigosView(TemplateView):  # Artigos
    template_name = "artigos.html"

class ContatoView(TemplateView):  # Contato
    template_name = "contato.html"

class Envio_artigosView(TemplateView):  # Envio Artigos
    template_name = "envio_artigos.html"

class FerramentasView(TemplateView):  # Ferramentas
    template_name = "ferramentas.html"

class IndexView(TemplateView):  # Página inicial
    template_name = "index.html"

class Mapa_siteView(TemplateView):  # Mapa Site
    template_name = "mapa_site.html"

class ModeloView(TemplateView):  # Modelo
    template_name = "modelo.html"

class NoticiasView(TemplateView):  # Noticias
    template_name = "noticias.html"

class Politica_direitos_autoraisView(TemplateView):  # Política de Direitos Autorais
    template_name = "politica_direitos_autorais.html"

class PublicidadeView(TemplateView):  # Publicidade
    template_name = "publicidade.html"

class SobreView(TemplateView):  # Sobre
    template_name = "sobre.html"

class Sofhie_sistemas_educacionaisView(TemplateView):  # Sofhie Sistemas Educacionais
    template_name = "sofhie_sistemas_educacionais.html"