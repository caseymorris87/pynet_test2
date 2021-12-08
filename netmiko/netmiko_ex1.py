#!/user/bin/env python3

from getpass import getpass
from netmiko import ConnectHandler

#password = getpass()
device1 = {
    'device_type': 'arista_eos',
    'host': 'arista1.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass'
}

device2 = {
    'device_type': 'juniper_junos',
    'host': 'vmx1.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass'
}

for con in (device1, device2):
    
    with ConnectHandler(**con) as net_connect:
    
        print(net_connect.find_prompt())

        if con['device_type'] == 'juniper_junos':
            conf_cmd = 'show configuration'
        elif con['device_type'] == 'arista_eos':
            conf_cmd = 'show run'        
 
        print(net_connect.send_command('show version'))
      
        conf_output = net_connect.send_command(conf_cmd)

        with open(f"{con['device_type']}_output.txt", 'w') as f:
            f.write(conf_output)
