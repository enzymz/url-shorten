from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.validators import URLValidator
from django.contrib.sites.models import Site
from django.contrib.gis.geoip import GeoIP
from datetime import date
from string import ascii_lowercase, ascii_uppercase, digits
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView

import hashlib
import random

from shorturl.forms import UrlForm
from shorturl.models import UrlShort, UserAgent
from shorturl.serializers import AgentSerializers


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
            except:
                return HttpResponse('Invaild link')
            if UrlShort.objects.filter(ori_link=url).exists():
                short_link = UrlShort.objects.get(ori_link=url).short_link
                #full_link = domain + '/shorturl/' + short_link

            else:
                url_short = UrlShort(ori_link  = url,
                                    hash_link = shorter(url),
                                  short_link= shorten())
                url_short.save()
                domain = get_domain()
                short_link = url_short.short_link
                #full_link = domain + '/shorturl/' + short_link
            return render(request, self.template_name, {'short_link': short_link}) # 'full_link': full_link -> context

        return render(request, self.template_name, {'form': form})


class GetLink(View):
    def get(self, request, *args, **kwargs):
        short_link = kwargs.get('short_link')
        long_url = UrlShort.objects.get(short_link=short_link)
        longurl = long_url.ori_link

        x_fordward_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_fordward_for:
            usr_ip = x_fordward_for.split(',')[0]
        else:
            usr_ip = request.META.get('REMOTE_ADDR')

        usr_agent = request.META.get('HTTP_USER_AGENT')

        geoip = GeoIP()
        if geoip.country(usr_ip)['country_name'] == None:
            usr_geo = 'Unknown'
        else: usr_geo = geoip.country(usr_ip)['country_name']
        user_info = UserAgent.objects.create(user_agent = usr_agent, 
                             short_link = long_url, user_ip = usr_ip,
                     user_national = usr_geo, date_create = date.today())
        user_info.save()
        return HttpResponseRedirect(longurl)

class AgentList(APIView):
    def get(self, request):
       start = request.GET.get('start')
       end = request.GET.get('end')
       useragent = UserAgent.objects.filter(date_create__range=[start, end])
       list_nation = [i.user_national for i in useragent]
       nation_dic = {}
       for i in set(list_nation):
           for c in list_nation:
               nation_dic[i] = list_nation.count(i)
       info = {'start': start, 'end': end,'countries': nation_dic, }
       return Response(info)


class AgentDetail():
    pass

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
