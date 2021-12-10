
import pyeapi
from getpass import getpass
from rich import print

password = getpass()

basedict = {
'transport': 'https',
'username': 'pyclass',
'password': password,
'port': '443'
}

con_list = []

for c,v in enumerate(range(1,5)):
    arista_con = basedict.copy()
    arista_con['host'] = f'arista{str(c+1)}.lasthop.io'
    con_list.append(arista_con)

print(con_list)

for device_dict in con_list:
    conn = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(conn)
    output = device.enable(['show lldp neighbors'])
    print()
    print(f'Host: {device_dict["host"]}')
    print(output[0]['result']['lldpNeighbors'])
