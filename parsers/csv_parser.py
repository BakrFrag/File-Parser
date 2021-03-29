#!/usr/bin/python3.8
import csv;
from .parser_helpers import ParserHelper,FileParserHelper;
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
    def read_csv(self,input_file,kind="customer"):
        """
        read data from csv file if exists
        """
        try:
            if FileParserHelper.check_file_exist(input_file):
                    csv_data=[];
        
                    with open(input_file,"r",encoding="utf-8") as csv_content:
                        rows=csv.DictReader(csv_content);
                        headers=rows.fieldnames;
                        if FileParserHelper.check_file_headers(headers,kind):
                                    for row in rows:
                                        if row not in csv_data:
                                             
                                               csv_data.append(row);
                                    return csv_data;
                        else:
                            return {"error":"file of type {} headers don't match".format(kind)};
            else:
                        return {"error":"file {} not exists".format(input_file)}
        except Exception as E:
                print(E.__class__.__name__)
                return {"error":"the file {} not valid csv file".format(input_file)};
                
    def generate_json_content(self):
        """
        transfer csv rows to list and generate json content which will be in parsing_result/simple.json
        """
        file_name="{}/{}".format(self.format,self.customers_file);
        self.customers_data=[list(row.values()) for row in self.customers_data]
        self.vehicles_data=[list(row.values()) for row in self.vehicles_data]
        return FileParserHelper.extract_customer_data(self.customers_data,self.vehicles_data,file_name);