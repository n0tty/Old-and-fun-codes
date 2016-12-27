#!/usr/bin/env python

import sys
import socket
import string

HOST="irc.server_name.net"
PORT=6667
NICK="chatur"
IDENT="ch4tUr"
REALNAME="ch4tUr"
CHAN="#channame"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Brain initiated"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Intelligence set"))

while 1:
  readbuffer=readbuffer+s.recv(1024)
  temp=string.split(readbuffer, "\n")
  readbuffer=temp.pop( )

  for line in temp:
    line=string.rstrip(line)
    line=string.split(line)

    if(line[0]=="PING"):
      s.send("PONG %s\r\n" % line[1])
