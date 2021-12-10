import pyeapi
from getpass import getpass
from rich import print

config = [
    'vlan 851',
    'name Casey1',
    'vlan 852',
    'name Casey2',
    'vlan 853',
    'name Casey3'
]


password = getpass()

basedict = {
'transport': 'https',
'username': 'pyclass',
'password': password,
'port': '443'
}

con_list = []

for c,v in enumerate(range(1,4)):
    arista_con = basedict.copy()
    arista_con['host'] = f'arista{str(c+1)}.lasthop.io'
    con_list.append(arista_con)

print(con_list)

for device_dict in con_list:
    conn = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(conn)
    cfg_output = device.config(config)
    output = device.enable(['show vlan'])
    print()
    print(output)
