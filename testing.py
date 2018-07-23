import pexpect
import sys
import time

ip_addr='10.22.162.42'
username='mfusion'
password='Cisco!23'
connection=pexpect.spawn('ssh {}@{}'.format(username, ip_addr), maxread=4000, logfile=sys.stdout, searchwindowsize=10000)
index=connection.expect(['Password', 'yes/no', pexpect.EOF, pexpect.TIMEOUT])

print connection.before
