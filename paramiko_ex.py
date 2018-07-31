
import paramiko
import re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('savbu-harness14',username='avsuser',password='insieme',key_filename='/dev/null')
si,so,se= ssh.exec_command('ls -l')
if so:
    output = so.readlines()
    print(output[0])

si,so,se= ssh.exec_command('ifconfig')
print(si)
print(so)
print(se)
if so:
    output = so.readlines()
    print(output)
    for line in output:
        if re.search(r'inet addr:\d+.\d+.\d+.\d+',line,re.I):
            print(line)
            break
ssh.close()

