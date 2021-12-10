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

            device.load_merge_candidate(filename='vlans.cfg')
            
            diff = device.compare_config()
            print(f'diff for host {host}:')
            print(diff)
            print('-'*70)

            if diff:
                print('committing')
                device.commit_config()
            else:
                print('no changes')
        
        print()
        

if __name__ == '__main__':
    main()            
