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
        if "error" in text_json.keys() or text_json.get("status") != "ok":
            return False

        return text_json.get("data")

    def creator_pdf(self):
        file = self.file_list[9]
        text_json = self._get_data(path_file=file)
        result = self._parser(text_json=text_json)

        text = ""
        for row in result:
            for key in row.keys():
                # print(key, row.get(key))
                text += "{}: {}\n".format(key, row.get(key))

        # print(text)
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Arial", "", "arialmt.ttf", uni=True)
        pdf.set_font("Arial", size=14)
        # text = pdf.normalize_text(txt=text)  # TODO
        # text.encode(encoding='UTF-8', errors='strict')
        pdf.cell(200, 10, txt=text)
        # pdf.cell(200, 10, txt=text.encode('utf-8').decode('latin-1'), ln=1, align='C')
        # Сохраняем созданный PDF-файл
        pdf.output(name="data.pdf")
        return result


if __name__ == "__main__":
    path = "TEST_DATA"
    result = CreatorPDF(path=path).creator_pdf()
    # print(len(result))
    # for key, value in result[0].items():
    #     print(key, ": ", value)
