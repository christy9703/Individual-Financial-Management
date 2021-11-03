import tika
from tika import parser
file = parser.from_file("/Users/caoyijun/Downloads/Data_IMG.JPG")
#print(file)

import textract
text = textract.process("/Users/caoyijun/Downloads/Data_IMG.JPG")

text_decode = text.decode('utf-8')

print(text_decode.split("\n"))
