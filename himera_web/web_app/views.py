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
    form_class = forms.QueryFormType
    template_name = "web_app/query_type.html"
    success_url = reverse_lazy('web_app:query-type')

    def post(self, request):
        form = forms.QueryFormType(request.POST)
        if form.is_valid():
            result = form.cleaned_data.get("query_type")
            print(result)
            if result == "aaa":
                return redirect(to="web_app:index")
        return super(self.__class__, self).post(request)
