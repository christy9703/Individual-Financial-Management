import pandas as pd
import os
import re

def filter_txt(line):
    filter_words=['', ' ']
    if (line not in filter_words):
        return True
    else:
        return False
    
file_path = "/Users/caoyijun/Individual-Financial-Management/bank statement parsed/"
file_name = os.listdir(file_path)

input_file = open(file_path + file_name[0], "r")
input_file_txt = input_file.read()

input_file_split = input_file_txt.strip().split("\n")
filter_list=[[''],[' ']]
print(len(input_file_split))
input_file_split_filtered=list(filter(filter_txt,input_file_split))
#print(input_file_split_filtered)
#print(len(input_file_split_filtered))

input_file_split_valuable = []
for line in input_file_split_filtered:
    if re.match(r'\d+/\d+/\d+', line):
        input_file_split_valuable.append(line)
    else:
        continue

r_date_list = []
r_amount_list = []
r_description_list = []
for elem in input_file_split_valuable:
    r_date = re.findall(r'\d+/\d+/\d+',elem)
    if r_date == []:
        r_date = None
    else:
        r_date=r_date[0]
    r_date_list.append(r_date)

    
    r_amount = re.findall(r"[-+]?([0-9]*\.[0-9]+|[0-9]+)", elem)
    if r_amount == []:
        r_amount = None
    else:
        r_amount = r_amount[0]
    r_amount_list.append(r_amount)
    elem.strip()
    r_description_list.append(elem)

    
df = pd.DataFrame(columns=['Date','Description','Amount'])

print(r_date_list)
print(r_amount_list)
print(r_description_list)

                  
    
