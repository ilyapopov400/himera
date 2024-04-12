from django.urls import path
from . import views

app_name = 'web_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('query-type/', views.QueryType.as_view(), name='query_type'),  # просмотр главной страницы
    path('query-type/name-standart', views.NameStandart.as_view(), name='name_standart'),  # по учетным данным

]
