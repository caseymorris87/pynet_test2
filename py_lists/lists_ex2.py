#!/usr/bin/env python3
ip_addr = input('Enter an IP address: ')

ip_addr = ip_addr.split('.')
ip_addr[-1] = '0'

ip_addr_bin = []

ip_addr_bin.append(bin(int(ip_addr[0])))
ip_addr_bin.append(bin(int(ip_addr[1])))
ip_addr_bin.append(bin(int(ip_addr[2])))
ip_addr_bin.append(bin(int(ip_addr[3])))

print(f'{ip_addr[0]:<12} {ip_addr[1]:<12} {ip_addr[2]:<12} {ip_addr[3]:<12}')
print(f'{ip_addr_bin[0]:<12} {ip_addr_bin[1]:<12} {ip_addr_bin[2]:<12} {ip_addr_bin[3]:<12}')
