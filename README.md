# SocketTcp_serverPython
Create a tcp socket for receiving incoming data from a sim900 module, using python and amason web service EC2 instance

Set UP service with Upstart

- move socketTCPpython.conf to /etc/init/
- move socketcp_gsm_py.py to /bin/

start service
- sudo start socketTCPpython

stop service
- sudo stop socketTCPpython

