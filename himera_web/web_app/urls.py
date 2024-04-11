from django.urls import path
from . import views

app_name = 'web_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы

]
