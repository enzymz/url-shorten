from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.validators import URLValidator
from django.contrib.sites.models import Site
from string import ascii_lowercase, ascii_uppercase, digits

import hashlib
import random

from .forms import UrlForm
from .models import UrlShort


class UrlView(View):
    """docstring"""
    form_class = UrlForm
    template_name = 'shorturl/short.html'
    show = 'shorturl/show.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        data = {}
        form = self.form_class(request.POST)

        if form.is_valid():
            url = form.cleaned_data['link']
            val = URLValidator()
            try:
                val(url)
                if  UrlShort.objects.filter(ori_link=url).exists():
                    short_link = UrlShort.objects.get(ori_link=url).short_link
                else:
                    url_short = UrlShort(ori_link  = url,
                                         hash_link = shorter(url),
                                         short_link= shorten())
                    url_short.save()

                    short_link = url_short.short_link
                return render(request, self.template_name, {'short_link': short_link})
            except:
                return HttpResponse('Invaild link')

        return render(request, self.template_name, {'form': form})


class GetLink(View):
    def get(self, request, *args, **kwargs):
        short_link = kwargs.get('short_link')
        long_url = UrlShort.objects.get(short_link=short_link)
        longurl = long_url.ori_link
        return HttpResponseRedirect(longurl)


def shorter(url):
    code_hash = hashlib.sha256(url.encode()).hexdigest()
    return code_hash


def shorten():
    flag = True
    while flag:
        str_pattern = ascii_lowercase + ascii_uppercase + digits
        random_7 = ''.join(random.choice(str_pattern)\
                for i in range(7))
        if not UrlShort.objects.filter(short_link=random_7).exists():
            flag = False
    return random_7

def get_domain():
    current_site = Site.objects.get_current()
    domain = current_site.domain
    return domain
