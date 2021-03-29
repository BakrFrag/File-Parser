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
            
            
            

        
        

        