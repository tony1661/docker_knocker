
import argparse
import socket
import time
import os
import select
from datetime import datetime

def knock(host, knock_seq, delay):
    """Knock host and port using tcp connection"""
    for port_proto in knock_seq:
        port = port_proto.split(':')[0]
        protocol = port_proto.split(':')[1]
        if protocol == 'tcp':
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setblocking(False)
                sock.connect_ex((host,int(port)))
                select.select([sock], [sock], [sock], 0)
                break
            except:
                print("Failure when trying to execute TCP Knock")
        else:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setblocking(False)
                sock.sendto(b'', (host,int(port)))
            except:
                print("Failure when trying to execute UDP Knock")

        sock.close()
        time.sleep(int(delay))
    time.sleep(int(interval)*60)
    

ip = os.getenv('IP', default='grandvista.duckdns.org')
ports = os.getenv('PORTS', default='1992:tcp,2991:udp').split(',')
interval = os.getenv('INTERVAL_IN_MIN', default='2')
delay = os.getenv('DELAY_IN_SEC', default='5')

while True:
    print(datetime.now())
    knock(ip, ports, delay)