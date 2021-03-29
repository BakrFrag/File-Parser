from ..parsers.xml_parser import XmlParser
import unittest;

class TestXmlParser(unittest.TestCase):
    """
    test XmlParser class
    """
    def setUp(self):
        self.xml_file="datasets/customer2.xml";
        self.xml_not_found="datasets/xml_not_found.xml"
    def test_read_xml(self):
        """
        test read xml file with xml file not found
        """
        xml_parser=XmlParser(self.xml_not_found);
        self.assertEqual(xml_parser['error'],"xml file {} not exist".format(self.xml_not_found));
    def test_extract_xml_data(self):
        """
        test extract_xml_data with customer file
        """
        xml_parser=XmlParser(self.xml);
        xml_data=xml_parser.extract_xml_data();
        self.assertTrue(xml_data.endswith("parsing_result/simple.json"));