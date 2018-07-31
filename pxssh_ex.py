


from pexpect import pxssh

import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input("hostname:")
    username = raw_input("username:")
    password = getpass.getpass('password:')
    s.login(hostname,username,password)
    s.sendline('uptime')
    s.prompt(['Password:','#','&'])
    print(s.before)
    s.sendline('ls -l')
    s.prompt(['$','#'])
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print('Pxssh fialed to login')
    print(e)
