from django.views.generic import TemplateView


class ChartForm(TemplateView):
    template_name = 'dash/dashboard.html'


