from rich import print
from napalm import get_network_driver
from my_devices import arista1, arista2, arista3, arista4

def main():
    for device in (arista1, arista2, arista3, arista4):
        
        driver = get_network_driver('eos')
        
        with driver(**device) as device:
            device.open()
            vlans = device.get_vlans()
            host = device.hostname
        
        print('-'*100)
        print(f'Host: {host}')
        print('-'*12)
        print(vlans)
        print('-'*100)
        print()
    
    print()

if __name__ == '__main__':
    main()            
