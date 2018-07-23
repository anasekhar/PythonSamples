import pexpect

child = pexpect.spawn('ssh %s@%s' % ('avsuser','savbu-harness14'),timeout=1500)
output = child.expect(['assword',"yes/no"],timeout=150)
if output ==0:
	child.sendline('insieme')
elif output == 1:
	child.sendline('yes')
	child.expect('assword:',timeout=150)
	child.sendline('insieme')
data = child.read()
print data


