import pandas as pd
import tika
from tika import parser
from datetime import date

def tika_parse_file(statement_path):
    statement_parsed = parser.from_file(statement_path)
    statement_content = statement_parsed["content"]
    return statement_content

def get_file(statement_path):
    statement_files = []
    for filename in os.listdir(statement_path):
        if 'eStmt' in str(filename) and '.pdf' in str(filename):
            statement_file = statement_path + str(filename)
        statement_files.append(statement_file)
    return statement_files



statement_path = "/Users/caoyijun/Individual-Financial-Management/bank statement/"
output_path = "/Users/caoyijun/Individual-Financial-Management/bank statement parsed/"
today =date.today().strftime("%m-%d-%Y")



for statement in get_file(statement_path):
    print("statement:"+statement)
    statement_name = statement.strip(statement_path).strip(".pdf")
    statement_content = tika_parse_file(statement)
    parsed_statement_name = statement_name + '_' + today + '.txt'
    print(parsed_statement_name)
    with open(output_path + parsed_statement_name,'w',encoding = 'utf-8') as file:
        file.write(statement_content)
        
