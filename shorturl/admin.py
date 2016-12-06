from django.contrib import admin
from .models import UrlShort, UserAgent
from django.contrib.admin import AdminSite


class ShortAdmin(admin.ModelAdmin):
    pass


class UserAgentAdmin(admin.ModelAdmin):
   pass


admin.site.register(UrlShort, ShortAdmin)
admin.site.register(UserAgent,UserAgentAdmin)
