from django import forms


class QueryFormType(forms.Form):
    query_type = forms.CharField(label="тип запроса", max_length=20)

