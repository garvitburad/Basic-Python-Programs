# First Program(Mobile number search)
import re

phoneNumberReg = re.compile(r'\+\d\d-\d{10}')
testCase = "hey my phone number is \"+91-9269775776\" and my whatsApp number is +91-9462239417"
a=(phoneNumberReg.findall(testCase))
print(phoneNumberReg.findall('Call on the 91-9828148115'))
for i  in range(siz(a)):
"""
# second program for finding Registration number and mobile number from a file
""" import re

regNo = re.compile(r'"\w+/\w+/\d\d/\d+"')
phoneNumberReg = re.compile(r'\d{10}')
f = open('data.js', 'r')
f.close()

for eachline in f:
    ##  print(eachline)
    = (phoneNumberReg.findall(eachline))
    # print(regNo.findall(eachline))
filter=re.compile((r'"\w+/\w+/\d\d/\d+"'))
print(filter.findall(result))
# third program
 identify names

import re
reg_ex=re.compile(r'\w+\s\w+')
test_string=('Garvit Burad  sfjssdfsd  a    jndskjd')
print()

print(reg_ex.findall(test_string))

