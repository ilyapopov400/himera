from django.shortcuts import render, redirect
from django.views import View
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

    # success_url = reverse_lazy('web_app:query_type')

    def post(self, request):
        form = forms.QueryTypeForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data.get("query_type")
            return redirect("{}/".format(result))
        return render(request=request,
                      template_name=self.template_name,
                      context={"form": form})


class Query(View):
    """
    поисковый запрос по полным учетным данным
    """

    def get(self, request, **kwargs):
        key = kwargs["type_q"]  # выбор формы для заполнения
        form = forms.query_form.get(key)
        template_name = "web_app/query.html"
        context = {"form": form}
        return render(request=request,
                      template_name=template_name,
                      context=context)

    def post(self, request, **kwargs):
        key = kwargs["type_q"]  # выбор формы для заполнения
        form = forms.query_form.get(key)(request.POST)
        template_name = "web_app/query.html"
        context = {"form": form}
        if form.is_valid():
            result = form.cleaned_data
            data = {
                key: result
            }
            print(data)  # TODO данные для запроса на API
            template_name = "web_app/index.html"  # TODO изменить на страницу с результатом запроса
            return render(request=request,
                          template_name=template_name,
                          context=context)
        return render(request=request,
                      template_name=template_name,
                      context=context)


class QueryResult(TemplateView):
    """
    страница с результатами поискового запроса
    """
    template_name = "web_app/query_result.html"
