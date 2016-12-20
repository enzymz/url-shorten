from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from shorturl.views import get_domain
from django.http import HttpResponse
from django.http import HttpResponse

class ChartForm(TemplateView):
    template_name = 'dash/index.html'
