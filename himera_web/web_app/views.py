from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.


class Index(TemplateView):
    '''
    стартовая страница приложения web_app
    '''
    template_name = 'web_app/index.html'
