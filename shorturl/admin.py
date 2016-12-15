from django.contrib import admin
from shorturl.models import UrlShort, UserAgent
from django.contrib.admin import AdminSite
from django import forms


class ShortAdmin(admin.ModelAdmin):
    pass


class UserAgentAdmin(admin.ModelAdmin):
    list_display = ['date_create']
    fields = ('user_agent', 'short_link', 'user_ip',
              'user_national','date_create')
    readonly_fields = ('date_create',)


admin.site.register(UrlShort, ShortAdmin)
admin.site.register(UserAgent,UserAgentAdmin)
