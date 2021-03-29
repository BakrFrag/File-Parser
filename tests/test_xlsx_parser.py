from parsers.xlsx_parser import XlsxParser;
import unittest;
class TestCsvParser(unittest.TestCase):
    """
    test xlsx parser
    """
    def setUp(self):
        self.valid_customers="datasets/customers.xlsx";
        self.csv_customer_headers_miss_match="customers_headers_error.xlsx";
        self.valid_vehicles="datasets/vehicles.xlsx";
        self.xlsx_vehicle_headers_miss_match="vehicles_headers_error.xlsx";
        self.xlsx_customers_not_exist="datasets/customers_not_exists.xlsx";
        self.xlsx_vehicles_not_exist="datasets/vehicles_not_exists.xlsx";