from django import forms

query_type_choices = [
    ("name_standart", "name_standart - стандартный запрос"),
    ("phone", "phone - запрос по телефону"),
    ("passport", "passport - запрос по паспорту"),
    ("inn_fl", "inn_fl - запрос по ИНН"),
    ("email", "email - запрос по электоронной почте"),
    ("snils", "snils - запрос по СНИЛС"),
    ("adres", "adres - запрос по адрессу"),
    ("avto", "avto - запрос по автомобилю"),
    ("vin", "vin"),
    ("inn", "inn"),
    ("ogrn", "ogrn"),
    ("scoring", "scoring"),
    ("credit", "credit"),
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


class PassportForm(forms.Form):
    passport = forms.CharField(label="паспорт", max_length=10, min_length=10)


class Inn_flForm(forms.Form):
    inn_fl = forms.CharField(label="номер ИНН физического лица", max_length=10, min_length=10)


class EmailForm(forms.Form):
    email = forms.CharField(label="адрес электоронной почты", max_length=20, min_length=2)


class SnilsForm(forms.Form):
    snils = forms.CharField(label="номер СНИЛС", max_length=11, min_length=11)


class AdresForm(forms.Form):
    city = forms.CharField(label="город", max_length=20, min_length=2)
    street = forms.CharField(label="улица", max_length=20, min_length=2)
    home = forms.CharField(label="дом", max_length=10, min_length=1)
    flat = forms.CharField(label="квартира", max_length=10, min_length=1)


class AvtoForm(forms.Form):
    avto = forms.CharField(label="номер автомобиля", max_length=9, min_length=8)


class VinForm(forms.Form):
    vin = forms.CharField(label="vin автомобиля", max_length=15, min_length=15)


class InnForm(forms.Form):
    inn = forms.CharField(label="ИНН", max_length=10, min_length=10)


class OgrnForm(forms.Form):
    ogrn = forms.CharField(label="ОГРН", max_length=13, min_length=13)


class ScoringForm(forms.Form):
    firstname = forms.CharField(label="имя", max_length=20, min_length=2)
    lastname = forms.CharField(label="фамилия", max_length=20, min_length=2)
    middlename = forms.CharField(label="отчество", max_length=20, min_length=2)
    birthday = forms.CharField(label="дата рождения (по формату: 01.01.1900)", max_length=10, min_length=10)


class CreditForm(forms.Form):
    firstname = forms.CharField(label="имя", max_length=20, min_length=2)
    lastname = forms.CharField(label="фамилия", max_length=20, min_length=2)
    middlename = forms.CharField(label="отчество", max_length=20, min_length=2)
    birthday = forms.CharField(label="дата рождения (по формату: 01.01.1900)", max_length=10, min_length=10)


query_form = {
    "name_standart": NameStandartForm,
    "phone": PhoneForm,
    "passport": PassportForm,
    "inn_fl": Inn_flForm,
    "email": EmailForm,
    "snils": SnilsForm,
    "adres": AdresForm,
    "avto": AvtoForm,
    "vin": VinForm,
    "inn": InnForm,
    "ogrn": OgrnForm,
    "scoring": ScoringForm,
    "credit": CreditForm,
}
