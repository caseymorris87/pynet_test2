from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, wait

def get_output(dev, cmd):
    with ConnectHandler(**con) as net_connect:
        return net_connect.send_command(cmd)


def main():

    password = os.getenv("PYNET_PASSWORD")
    if not password:
        password = getpass('password? ')

    devices = [
        {
            "host": "arista1.lasthop.io",
            "device_type": "arista_eos",
            "username": "pyclass",
            "password": password,
        },
        {
            "host": "arista2.lasthop.io",
            "device_type": "arista_eos",
            "username": "pyclass",
            "password": password,
        },
        {
            "host": "arista3.lasthop.io",
            "device_type": "arista_eos",
            "username": "pyclass",
            "password": password,
        },
        {
            "host": "arista4.lasthop.io",
            "device_type": "arista_eos",
            "username": "pyclass",
            "password": password,
        },
    ] 

    pool = ThreadPoolExecutor(max_workers=4)
    futures = []

    for dev in devices:
        


if __name__ == '__main__':
    main()


    
