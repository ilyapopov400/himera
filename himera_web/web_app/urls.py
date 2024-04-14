from django.urls import path
from . import views

app_name = 'web_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('query-type/', views.QueryType.as_view(), name='query_type'),  # просмотр страницы с выбором типа запроса
    path('query-type/<str:type_q>/', views.Query.as_view()),  # по выбранным типам запроса
    path('query-result/', views.QueryResult.as_view()),  # страница результата запроса

]
