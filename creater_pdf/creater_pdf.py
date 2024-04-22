import os
import json
from fpdf import FPDF


class CreatorPDF:
    def __init__(self, path: str):
        """

        :param path: путь к директории с результатами запроса
        :self.file_list : список файлов в директории
        """
        self.path = path
        self.file_list = list(map(lambda x: "{}/{}".format(path, x), os.listdir(path=path)))

    def _get_data(self, path_file):
        """

        :param path_file:
        :return: результат чтения файла
        """
        with open(file=path_file, mode="r", encoding="utf-8") as file:
            text_json = json.loads(file.read())

        return text_json

    def _parser(self, text_json: dict):
        """
        парсинг данных с одного файла
        :param text_json:
        :return: list
        """
        # if "error" in text_json.keys() or text_json.get("status") != "ok":
        #     return [{"Нет данных": ""}, ]

        if text_json.get("status") == "ok":
            return text_json.get("data")
        else:
            result = list()
            result.append(text_json)
            return result

    def creator_pdf(self, file):
        text_json = self._get_data(path_file=file)
        result = self._parser(text_json=text_json)

        text = list()
        text.append("HIMERA")
        for row in result:
            for key in row.keys():
                text.append(
                    "{}: {}".format(key, row.get(key))
                )

        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Arial", "", "arialmt.ttf", uni=True)
        pdf.set_font("Arial", size=14)
        for row in text:
            pdf.cell(200, 10, txt=row, ln=1, align='C')

        # Сохраняем созданный PDF-файл
        pdf.output(name="data.pdf")
        return result

    def __call__(self):
        for e, file in enumerate(self.file_list):
            try:
                self.creator_pdf(file=file)
            except:
                print(e, file)
        number_file = 8
        print(self.file_list[number_file])
        file = self.file_list[number_file]  # TODO для одного файла, далее циклом по всем
        self.creator_pdf(file=file)


if __name__ == "__main__":
    path = "TEST_DATA"
    result = CreatorPDF(path=path)()
