
#Create a script that verifies if the string is a phone number with the following formats (see below).

_mytest ="""
ALl values (123) - 1234 - 123a
123 - 1234 - 1234
123 - 1234 - 1234
(123) - 1234 - 123  
(123) . 1234 - 125a
706.540.3309
"""


import re
phone_num = re.findall(r'(\d{3}\s*(\.|-)\s*\d{3}\s*(\.|)-\s*\d{4}\b)',_mytest)


l=[]
print(phone_num)
#l.extend([number[0] for number in phone_num])
#l.extend([number[0] for number in phone_num1])
#print(l)
