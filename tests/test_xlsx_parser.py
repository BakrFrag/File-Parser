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

    def test_with_file_not_exist(self):
        """
        test XlsxParser with file not exist
        """
        xlsx_parser=xlsxParser(self.valid_customers,self.xlsx_vehicles_not_exist);
        function_result=xlsx_parser.read_xlsx(self.vehicles_file,kind="vehicle");
        self.assertEqual(function_result['error'],"file {} not exists".format(self.xlsx_vehicles_not_exist));

        xlsx_parser=XlsxParser(self.xlsx_customers_not_exist,self.valid_vehicles);
        function_result=xlsx_parser.read_xlsx(self.customers_file,kind="customer");
        self.assertEqual(function_result['error'],"file {} not exists".format(self.xlsx_vehicles_not_exist));