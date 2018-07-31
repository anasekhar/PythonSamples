
import pexpect

child = pexpect.spawn('ssh avsuser@savbu-harness14')
output = child.expect(["yes/no","Password"],timeout=200)
if output:
    if output==0:
        child.sendline('yes')
        val = child.expect(["Password"],timeout=10)
        if val==0:
            child.sendline('ijsieme')
        else:
            print("no password apperad")
    elif output ==1:
        child.sendline('insieme')
_output = child.expect(['.*#',"$"],timeout=10)
if _output:
    child.sendline('ls -ltr')
    print(child.before())
    print(child.after())


