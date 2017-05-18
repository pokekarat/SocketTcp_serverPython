#!/usr/bin/env python

import socket
import sys
import os, time

os.environ['TZ'] = 'America/Lima'
time.tzset()

TCP_IP = '172.31.46.42'
TCP_PORT = 50000
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 1:
        conn, addr = s.accept()
        print 'Connection address:', addr
        hora = time.strftime('%X')
        year = time.strftime('%Y')
        month = time.strftime('%m')
        day = time.strftime('%d')

        datafile = open('/var/www/html/DATAserver/Dataset_'+hora+'_'+day+':'+month+':'+year+'.dat','w')

        while 1:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                print "received data:", data
                conn.send(data)  # echo
                datafile.write(data+'\n')
        datafile.close()
conn.close()

