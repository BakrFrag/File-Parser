#!/usr/bin/python3.8
import xlrd
from .parser_helpers import ParserHelper, FileParserHelper


class XlsxParser(object):
    """
    init parameters used to parse xlsx file
    """

    def __init__(self, customers, vehicles):
        self.format = "xlsx"
        self.customers_file = customers
        self.vehicles_file = vehicles
        self.customers_data = []
        self.vehicles_data = []

    def read_xlsx(self, input_file, kind="customer"):
        """
        parse xlsx file and read data if exists
        """
        try:
            if FileParserHelper.check_file_exist(input_file):
                xlsx_data = []
                xlsx_workbook = xlrd.open_workbook(input_file)
                xlsx_sheet = xlsx_workbook.sheet_by_index(0)
                headers = xlsx_sheet.row_values(0)
                if FileParserHelper.check_file_headers(headers, kind):
                    xlsx_rows = xlsx_sheet.nrows
                    for i in range(1, xlsx_rows):
                        row = xlsx_sheet.row_values(i)
                        if row not in xlsx_data:
                            xlsx_data.append(row)
                    return xlsx_data
                else:
                    return {"error": "file of type {} headers don't match".format(kind)}
            else:
                return {"error": "file {} not exists".format(input_file)}

        except Exception as E:
            return {"error": "the file {} not valid xlsx file".format(input_file)}

    def generate_json_content(self):
        """
        generate json content from parsed xlsx file 
        result in parsing_result/simple.json
        """
        file_name = "{}/{}".format(self.format, self.customers_file)
        return FileParserHelper.extract_customer_data(
            self.customers_data, self.vehicles_data, file_name)
