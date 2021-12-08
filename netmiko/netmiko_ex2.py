from netmiko import ConnectHandler



def configure_stuff(net_connect, configs):
    return net_connect.send_config_set(configs)


def main():

    configs = (
        'ntp server 130.126.24.21 use-vrf management',
        'ntp server 152.2.21.1 use-vrf management'
    )

    device = {
        'device_type': 'cisco_nxos',
        'host': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': '88newclass',
        'port': '22'
    }

    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
        output = configure_stuff(net_connect, configs)       
        print(output)

if __name__ == '__main__':
    main()
