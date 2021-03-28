#!/usr/bin/python3.8;
import untangle;
class XmlParser(object):
    def __init__(self,input_file,export_format="xml"):
        self.input_file=input_file;
        self.export_format=export_format;
        self.file_data="";
    