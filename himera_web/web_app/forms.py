from django import forms

query_type_choices = [
    ("name_standart", "name_standart - стандартный запрос"),
    ("phone", "phone"),
    ("3", "passport"),
    ("4", "inn_fl"),
    ("5", "email"),
    ("6", "snils"),
    ("7", "adres"),
    ("8", "avto"),
    ("9", "vin"),
    ("10", "inn"),
    ("11", "ogrn"),
    ("12", "scoring"),
    ("13", "credit"),
]


class QueryTypeForm(forms.Form):
    query_type = forms.ChoiceField(label="тип запроса", choices=query_type_choices)


class NameStandartForm(forms.Form):
    firstname = forms.CharField(label="имя", max_length=20, min_length=2)
    lastname = forms.CharField(label="фамилия", max_length=20, min_length=2)
    middlename = forms.CharField(label="отчество", max_length=20, min_length=2)
    day = forms.CharField(label="день", max_length=2, min_length=2)
    mounth = forms.CharField(label="месяц", max_length=2, min_length=2)
    year = forms.CharField(label="год", max_length=4, min_length=4)


class PhoneForm(forms.Form):
    phone = forms.CharField(label="телефон", max_length=11, min_length=11)
