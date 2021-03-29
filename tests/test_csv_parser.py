from parsers.csv_parser import CsvParser;
import unittest;
class TestCsvParser(unittest.TestCase):
    def setUp(self):
        self.valid_customers="datasets/customers.csv";
        self.csv_customer_headers_miss_match="customers_headers_error.csv";
        self.valid_vehicles="datasets/vehicles.csv";
        self.csv_vehicle_headers_miss_match="vehicles_headers_error.csv";
        self.csv_customers_not_exist="datasets/customers_not_exists.csv";
        self.csv_vehicles_not_exist="datasets/vehicles_not_exists.csv";
    def test_with_file_not_exist(self):
        """
        test CsvParser with file not exist
        """
        csv_parser=CsvParser(self.valid_customers,self.csv_vehicles_not_exist);
        function_result=csv_parser.read_csv(self.vehicles_file,kind="vehicle");
        self.assertEqual(function_result['error'],"file {} not exists".format(self.csv_vehicles_not_exist));

        csv_parser=CsvParser(self.csv_customers_not_exist,self.valid_vehicles);
        function_result=csv_parser.read_csv(self.customers_file,kind="customer");
        self.assertEqual(function_result['error'],"file {} not exists".format(self.csv_vehicles_not_exist));
    def test_with_headers_miss_match(self):
        """
        test CsvParser with customer and vehicle file headers miss match
        """
        csv_parser=CsvParser(self.valid_customers,self.csv_vehicle_headers_miss_match);
        function_result=csv_parser.read_csv(self.vehicles_file,kind="vehicle");
        self.assertEqual(function_result['error'],"file of type vehicle headers don't match");


        csv_parser=CsvParser(self.csv_customer_headers_miss_match,self.valid_vehicles);
        function_result=csv_parser.read_csv(self.customers_file,kind="vehicle");
        self.assertEqual(function_result['error'],"file of type customer headers don't match");