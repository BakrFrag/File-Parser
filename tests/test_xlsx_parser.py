from parsers.xlsx_parser import XlsxParser;
import unittest;
class TestxlsxParser(unittest.TestCase):
    """
    test xlsx parser
    """
    def setUp(self):
        self.valid_customers="datasets/customers.xlsx";
        self.xlsx_customer_headers_miss_match="datasets/customers_headers_error.xlsx";
        self.valid_vehicles="datasets/vehicles.xlsx";
        self.xlsx_vehicle_headers_miss_match="datasets/vehicles_headers_error.xlsx";
        self.xlsx_customers_not_exist="datasets/customers_not_exists.xlsx";
        self.xlsx_vehicles_not_exist="datasets/vehicles_not_exists.xlsx";

    def test_with_file_not_exist(self):
        """
        test XlsxParser with file not exist
        """
        xlsx_parser=XlsxParser(self.valid_customers,self.xlsx_vehicles_not_exist);
        function_result=xlsx_parser.read_xlsx(xlsx_parser.vehicles_file,kind="vehicle");
        self.assertEqual(function_result['error'],"file {} not exists".format(self.xlsx_vehicles_not_exist));

        xlsx_parser=XlsxParser(self.xlsx_customers_not_exist,self.valid_vehicles);
        function_result=xlsx_parser.read_xlsx(xlsx_parser.customers_file,kind="customer");
        self.assertEqual(function_result['error'],"file {} not exists".format(self.xlsx_customers_not_exist));
    
    def test_with_headers_miss_match(self):
        """
        test xlsxParser with customer and vehicle file headers miss match
        """
        xlsx_parser=XlsxParser(self.valid_customers,self.xlsx_vehicle_headers_miss_match);
        function_result=xlsx_parser.read_xlsx(xlsx_parser.vehicles_file,kind="vehicle");
        self.assertEqual(function_result['error'],"file of type vehicle headers don't match");


        xlsx_parser=XlsxParser(self.xlsx_customer_headers_miss_match,self.valid_vehicles);
        function_result=xlsx_parser.read_xlsx(xlsx_parser.customers_file,kind="customer");
        self.assertEqual(function_result['error'],"file of type customer headers don't match");

    def test_xlsx_generate_json_content(self):
        """
        test xlsxParser with a valid customer and vehicle file
        """
        xlsx_parser=XlsxParser(self.valid_customers,self.valid_vehicles);
        function_result=xlsx_parser.generate_json_content();
        self.assertTrue(function_result.endswith("parsing_result/simple.json"));