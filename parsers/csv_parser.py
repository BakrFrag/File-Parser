#!/usr/bin/python3.8
import csv;
from helpers import ParserHelper,FileParserHelper;
class CsvParser(object):
    """
    init parameters used to parse csv data  
    """
    def __init__(self,customers,vehicles):
              self.format="csv";
              self.customers_file=customers;
              self.vehicles_file=vehicles;
              self.customers_data=[];
              self.vehicles_data=[];
    