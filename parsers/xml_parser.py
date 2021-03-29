#!/usr/bin/python3.8;
import untangle
from .parser_helpers import ParserHelper, FileParserHelper


class XmlParser(object):
    def __init__(self, input_file, export_format="xml"):
        self.input_file = input_file
        self.export_format = export_format
        self.file_data = ""

    def read_xml_file(self):
        """
        read and parse xml file
        """
        try:
            if FileParserHelper.check_file_exist(self.input_file):
                self.file_data = untangle.parse(self.input_file)
            else:
                return {"error": "xml file {} not exist".format(self.input_file)}

        except Exception as E:
            return {"error": "invalid xml file "}

    def extract_xml_vehicles(self, units):
        vehicles_number = len(units)
        vehicles_data = units.Vehicle
        if vehicles_number == 1:
            vehicle = {}
            vehicle['id'] = vehicles_data['id']
            vehicle['make'] = vehicles_data.Make.cdata
            vehicle['vim_number'] = vehicles_data.VinNumber.cdata
            return vehicle
        else:
            vehicles = []
            for i in range(vehicles_number):
                vehicle = {}
                vehicle['id'] = vehicles_data[i]['id']
                vehicle['make'] = vehicles_data[i].Make.cdata
                vehicle['vim_number'] = vehicles_data[i].VinNumber.cdata
                vehicles.append(vehicle)
            return vehicles

    def extract_xml_data(self):
        """
        extract customer and vehicle data from xml file
        """
        xml_data = {}
        xml_data['file_name'] = "{}/{}".format(
            self.export_format, self.input_file)
        xml_data['transaction'] = {}
        date = self.file_data.Transaction.Date.cdata
        xml_data['transaction']['date'] = date
        customer = self.file_data.Transaction.Customer
        customer_id = customer['id']
        customer_name = customer.Name.cdata
        customer_address = customer.Address.cdata
        customer_phone = customer.Phone.cdata
        xml_data['transaction']['customer'] = {
            "id": customer_id,
            "name": customer_name,
            "address": customer_address,
            "phone": customer_phone}
        xml_data['transaction']['vehicles'] = self.extract_xml_vehicles(
            customer.Units)
        return FileParserHelper.export_to_json(xml_data)
