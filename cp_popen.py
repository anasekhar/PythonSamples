import os

file_name ='test.txt'
os.popen('cp {} {}'.format(file_name,"testcopy.txt"))
print os.listdir(os.getcwd())
