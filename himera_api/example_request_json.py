"""
пример для json запроса к ChangeRequest
"""

data = {
    "name_standart": {
        # Запрос по ФИО
        "firstname": "Иванов",  # - имя, - обязательное
        "lastname": "Иван",  # - фамилия, - обязательное
        "middlename": "Иванович",  # - отчество, - обязательное
        "day": "01",  # - день рождения
        "mounth": "01",  # - месяц рождения
        "year": "1900",  # - год рождения
    },
    "phone": {
        # Запрос по телефону
        "phone": "79123456789"  # номер телефона
    },
    "passport": {
        # Запрос по паспорту
        "passport": "1234567890"  # - серия и номер паспорта без пробелов
    },

    "inn_fl": {
        # Запрос по ИНН физ.лиза
        "inn_fl": "1234567890"  # - номер ИНН
    },
    "email": {
        # Запрос по E-mail
        "email": "demo@demo.ru"  # - почта
    },
    "snils": {
        #  Запрос по СНИЛС
        "snils": "1234567890"  # - снилс
    },
    "adres": {
        #  Запрос по адресу
        "city": "москва",  # - город
        "street": "пушкина",  # - улица
        "home": "17",  # - дом
        "flat": "3",  # - квартира
    },
    "avto": {
        # Запрос по номеру авто
        "avto ": "A777AA77",  # - номер авто (по формату: A777AA77 кирилицей)
    },
    "vin": {
        # Запрос по VIN
        "vin", "kgft5l05lfds46d"  # - VIN номер авто
    },
    "inn": {
        # Запрос по ИНН
        "inn": "1234567890"  # - инн
    },
    "ogrn": {
        # Запрос по ОГРН
        "ogrn": "1027739642281"  # ОГРН
    },
    "scoring": {
        # Скоринг
        "firstname": "иван",  # - имя
        "lastname": "иванов",  # - фамилия
        "middlename": "иванович",  # - отчество
        "birthday": "01.01.1900",  # дата рождения (по формату: 01.01.1900)

    },
    "credit": {
        # Запрос кредитного рейтинга
        "firstname": "иван",  # - имя
        "lastname": "иванов",  # - фамилия
        "middlename": "иванович",  # - отчество
        "birthday": "01.01.1900",  # - дата рождения (по формату: 01.01.1900)
    },
}

if __name__ == "__main__":
    pass
