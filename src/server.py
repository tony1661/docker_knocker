
import argparse
import socket
import time
import os
import select

def knock(host, knock_seq, delay):
    """Knock host and port using tcp connection"""
    for port_proto in knock_seq:
        port = port_proto.split(':')[0]
        protocol = port_proto.split(':')[1]
        print(port + ' ' + protocol)
        if protocol == 'tcp':
            print("using TCP")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)
            sock.connect_ex((host,int(port)))
            select.select([sock], [sock], [sock], 0)
        else:
            print("using UDP")
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setblocking(False)
            sock.sendto(b'', (host,int(port)))

        sock.close()
        time.sleep(int(delay))
    time.sleep(int(interval))

ip = os.getenv('IP', default='grandvista.duckdns.org')
ports = os.getenv('PORTS', default='1992:tcp,2991:udp').split(',')
interval = os.getenv('INTERVAL_IN_MIN', default='60')
delay = os.getenv('DELAY_IN_SEC', default='5')

while True:
    knock(ip, ports, delay)