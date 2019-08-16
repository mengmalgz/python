#!/usr/bin/python
#Filename:pxssh.py

import pxssh
s = pxssh.pxssh()
if not s.login ('192.168.1.35', 'root', ' '):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    s.sendline ('ls -l')
    s.prompt()         # match the prompt
    print s.before     # print everything before the prompt.
    s.logout()
