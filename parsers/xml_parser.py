#!/usr/bin/python3.8;
import untangle;
from parser_helpers import ParserHelper,FileParserHelper;
class XmlParser(object):
    def __init__(self,input_file,export_format="xml"):
        self.input_file=input_file;
        self.export_format=export_format;
        self.file_data="";
    def read_xml_file(self):
        try:
            if FileParserHelper.check_file_exist(self.input_file):
                self.file_data=untangle.parse(self.input_file);
            else:
                return {"error":"xml file {} not exist".format(self.input_file)};

        except Exception as E:
            return {"error":"invalid xml file "};
    