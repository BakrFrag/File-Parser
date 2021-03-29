#!/usr/bin/python3.8
from parser import csv_parser,xlsx_parser,xml_parser;
import sys;
class ParserHandler(object):
    """
    handle parsed arguments
    """
    FORMATS=["xml","csv","xlsx"];
    XML_FORMAT="to parse xml file ./parser.py xml xml_file_path.xml";
    CSV_FORMAT="to parse csv file ./parser.py csv csv_customer_file_path.csv csv_vehicles_file_path.csv";
    XLSX_FORMAT="to parse xlsx file ./parser.py xlsx xlsx_customer_file_path.xlsx xlsx_vehicles_file_path.xlsx"
    def __init__(self,arguments):
        """
        init parameters
        """
        self.arguments=sys.argv;
        self.length=len(self.arguments);
        self.handle_arguments();
    def xml_handler(self,format,customer_file):
        """
        apply xml parser on arguments
        """
        xml_parser=XmlParser(customer_file,format);
        parse_xml=xml_parser.read_xml_file();
        if type(parse_xml) is dict:
            return parse_xml['error'];
        else:
           return xml_parser.extract_xml_data();
           
    def csv_handler(self,format,customer_file,vehicle_file):
        """
        apply csv parser in arguments
        """
        csv_parser=CsvParser(customer_file,vehicle_file);
        csv_customer_data==csv_parser.read_csv(csv_parser.customers_file,kind="customer");
        if type(csv_customer_data) is dict:
            return csv_customer_data['error'];
        csv_parser.customers_data=csv_customer_data;
        csv_vehicle_data=csv_parser.read_csv(csv_parser.vehicles_file,kind="vehicle")
        if type(csv_vehicle_data) is dict:
            return csv_vehicle_data['error'];
        csv_parser.vehicle_file_data=csv_vehicle_data;
        csv_parser.vehicles_data=csv_vehicle_data;
        return csv_parser.generate_json_content();


    def handle_arguments(self):
        """
        handle arguments and apply right parser 
        """
        if self.length < 3:
            return "too less arguments";
        elif self.length > 4:
            return "to manay arguments";
        format=self.arguments[1];
        customer_file=self.arguments[2]
        elif format not in FORMAT:
            return "not supported format"
        elif self.length == 3 and format=="xml":
              return self.xml_handler(format,customer_file);
        elif self.length == 4:
            vehicle_file=self.arguments[3];
            if format=="csv":
                return self.csv_handler(format,customer_file,vehicle_file);
            elif format=="xlsx":
                return self.xlsx_handler(format,customer_file,vehicle_file);
            
            
            

        
        

        