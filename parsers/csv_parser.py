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
     def read_csv(self,input_file,kind="customer"):
        """
        read data from csv file if exists
        """
        try:
            if FileParserHelper.check_file_exist(input_file):
                    csv_data=[];
                    with open(input_file,"r") as csv_content:
                        rows=csv.DictReader(csv_content);
                        headers=rows.fieldnames;
                        print(headers)
                        if FileParserHelper.check_file_headers(headers,kind):
                                    print("headers matched")
                                    for row in rows:
                                        if row not in csv_data:
                                             
                                               csv_data.append(row);
                                    return csv_data;
                        else:
                            return {"error":"file of type {} headers don't match".format(kind)};
            else:
                        return {"error":"file {} not exists".format(input_file)}
        except Exception as E:
                return {"error":"the file {} not valid csv file".format(input_file)};