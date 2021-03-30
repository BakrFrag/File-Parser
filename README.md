# File-Parser
parse files with different formats and export data in json format 
## Output
- parsed files data export in json format and located on current_working_directory/parsing_result/simple.json 
- if folder parsing_result not found it will be created 
- if file simple.json exist it will overwrite it 
- if file simple.json not exist it will create it 
## Prerequests 
- software packages are necessary to run this project 
- [Git version control language](https://git-scm.com/) 
- [python software version 3.8.5](https://docs.python.org/release/3.8.5/)
- [pip3 python3 package index](https://pypi.org/project/pip/)
## How To Run

1. clone project from github 
```
git clone https://github.com/BakrFrag/File-Parser
```
2. go to inside project file 
```bash
cd File-Parser
```
3. install libraries used in project 
```
pip3 install -r requirements.txt
```
or
```
pip3 install xlrd==1.2.0
```
```
pip3 install untangle==1.1.1
```
4. add executable permission to file parser.py 
```
sudo chmod +x parser.py
```
5. if you want to run tests 
```
python3.8 -m unittest
```
6. start use parser.py and parse files

## Parsing Files 

- script handle arguments from command line 
- in case of csv and xlsx format customers file has to be parsed first 
- files headers must match 
- if exception will parse files happen it will printed on terminal exception like parse files with headers miss match , invalid file or file not exist 
- if files parsed it will return the path to parsing output
- if xlsx customers has to be in first sheet in first workbook and vehicles has to be in first sheet in second workbook
- in case of csv format or xlsx format vehicles related to customer extracted by joining vehicle.owner_by == customer.id

1. to parse xml file 
```
./parser.py xml xml_file.xml
```
2. to parse csv file 
```
./parser.py csv customers_file.csv vehicles_file.csv
```
3. to parse xlsx workbook
```
./parser.py xlsx customers_file.xlsx vehicles_file.xlsx
```
## File Structure
1. parsers directory include parser classes used to parse different file formats like xslsx csv and xml 
parser_helper include utlity functions used by any parser 
3. tests directory include unittests for parser classess 
4. parser.py handle script arguments and apply right parser on them 

## Deveopment
- this script is developed in enviroment with Ubuntu 20.04 relase
- all file formatted using [pep8](https://pypi.org/project/autopep8/)  
- each method or class include description about it 
