from django.conf.urls import url
from shorturl.views import UrlView, GetLink


urlpatterns = [
    url(r'^$', UrlView.as_view()),
    url(r'^(?P<short_link>[a-zA-Z0-9]+)/$', GetLink.as_view(), name='getlink'),	
]