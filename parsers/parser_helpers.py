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
    