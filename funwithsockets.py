#/usr/bin/python

import socket

print "Does the platform support IPv6?"
print socket.has_ipv6

print "Lets look up a host by name!"
print socket.gethostbyname("www.google.com")
