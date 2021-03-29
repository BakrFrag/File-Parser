#!/usr/bin/python3.8
from parser import csv_parser,xlsx_parser,xml_parser;
import sys;
class ParserHandler(object):
    """
    handle parsed arguments
    """
    FORMATS=["xml","csv","xlsx"];
    def __init__(self,arguments):
        self.arguments=sys.argv;
        self.length=len(self.arguments);
        self.handle_arguments();
        