from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from . import forms


# Create your views here.


class Index(TemplateView):
    '''
    стартовая страница приложения web_app
    '''
    template_name = "web_app/index.html"


class QueryType(FormView):
    """
    странца выбора поискового запроса
    """
    form_class = forms.QueryTypeForm
    template_name = "web_app/query_type.html"
    success_url = reverse_lazy('web_app:query_type')

    def post(self, request):
        form = forms.QueryTypeForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data.get("query_type")
            print(result)  # TODO
            if result == "name_standart":
                return redirect(to="web_app:{}".format(result))
        return super(self.__class__, self).post(request)


class NameStandart(FormView):
    """
    поисковый запрос по полным учетным данным
    """
    form_class = forms.NameStandartForm
    template_name = "web_app/name_standart.html"
    success_url = reverse_lazy('web_app:index')

    def post(self, request):
        form = forms.NameStandartForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            print(result)  # TODO данные для запроса на API
        return super(self.__class__, self).post(request)