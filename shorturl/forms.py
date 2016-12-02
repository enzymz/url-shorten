from django import forms


class UrlForm(forms.Form):
    link = forms.CharField(max_length=255)
    #short_link = forms.TextField(label='Shorten link', max_length=50)
