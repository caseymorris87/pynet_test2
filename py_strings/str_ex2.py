#!/usr/bin/env python3
ip_addr = input('Enter an IP address: ')

ip_addr = ip_addr.split('.')

print(f'{ip_addr[0]:<12} {ip_addr[1]:<12} {ip_addr[2]:<12} {ip_addr[3]:<12}')
