#!/usr/bin/python3.8
import os;
import json;
class ParserHelper(object):
    """
    include utlity functions used by any parser like 
           - create folder parsing_result if not exist
           - generate file path parsing_result/simple.json
    """
    FOLDER_NAME="parsing_result"
    CURRENT_DIRECTORY=os.getcwd();
    @staticmethod
    def create_folder_if_not_exist():
        """
        create folder parsing_result if not exist
        """
        full_path=os.path.join(
            ParserHelper.CURRENT_DIRECTORY,
            ParserHelper.FOLDER_NAME);
        if not os.path.exists(full_path):
            os.mkdir("parsing_result");
     @staticmethod  
    def generate_file_path():
        """
        generate full path to parsing_result/simple.json to write parsing result 
        """
        ParserHelper.create_folder_if_not_exist();
        return os.path.join(os.path.join(
            ParserHelper.CURRENT_DIRECTORY,
            ParserHelper.FOLDER_NAME),
            "simple.json");
    
class FileParserHelper(object):
    """
    include utlity functions used by any file parser 
    utility functions like 
         - check file headers
         - check file exists 
         - extract customer data
         - extract vehicles related to specfic customer
    """
    CUSTOMER_HEADERS=['id', 'name', 'address', 'phone', 'date'];
    VEHICLE_HEADERS=['id', 'make', 'vin_number', 'owner_id']
    @staticmethod
    def check_file_exist(file_location):
        """
        check if parsed argument file exists or not 
        """
        return os.path.isfile(file_location);

    @staticmethod
    def check_file_headers(headers,kind="customer"):
        """
        check file headers in customer and vehicle
        """
        headers=[i.lower() for i in headers];
        if kind=="customer":
            return headers==FileParserHelper.CUSTOMER_HEADERS;
        else:
            return headers==FileParserHelper.VEHICLE_HEADERS;
    @staticmethod
    def extract_customer_vehicles(vehicles):
        """
        get vehicles related to specfic customer by joining 
        vehicle[owner_id] and customer[id]
        """
        
        def get_related_vehicles(customer_id):
            related_vehicles=[];
            for vehicle in vehicles:
                if vehicle[3]==customer_id:
                        vehicle_data={
                        "id":vehicle[0],
                        "make":vehicle[1],
                        "vin_number":vehicle[2]
                        };
                        related_vehicles.append(vehicle_data);
            if len(related_vehicles)==1:
                return related_vehicles[0];
            else:
                return related_vehicles;
        return get_related_vehicles;

    @staticmethod
    def extract_customer_data(customers,vehicles,file_name):
        
        """
        extract customer fields data
        """
        customer_related_vehicles=FileParserHelper.extract_customer_vehicles(vehicles);
        customer_json={"file_name":file_name};
        customer_json['transaction']=[];
        for customer in customers:
                customer_id=customer[0];
                customer_name=customer[1];
                customer_address=customer[2];
                customer_phone=customer[3];
                customer_date=customer[4];
                customer_vehicles = customer_related_vehicles(customer_id);
                customer_json['transaction'].append({
                    "date":customer_date.replace("/","-"),
                    "customer":{
                        "id":customer_id,
                        "name":customer_name,
                        "address":customer_address,
                        "phone":customer_phone
                    },
                    
                        "vehicles":customer_vehicles
                    
                });
        
        return FileParserHelper.export_to_json(customer_json);

    @staticmethod
    def export_to_json(json_content):
        """
        write json content  to parsing_result/simple.json
        """
        json_file_path=ParserHelper.generate_file_path();
        with open(ParserHelper.generate_file_path(),"w") as json_file:
            json_file.write(json.dumps(json_content,indent=4));
        return json_file_path;