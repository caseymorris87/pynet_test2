class NetDevice():

    def __init__(self, ip_addr, username, password, serial_num=None, model=None, vendor=None, uptime=None, os_version=None):
        
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.serial_num = serial_num
        self.model = model
        self.vendor = vendor
        self.uptime = uptime
        self.os_version = os_version

def main():
    
    obj_list = [
        NetDevice('10.10.10.10', 'admin', 'pass'),
        NetDevice('1.1.1.1', 'admin', 'my_pass'),
        NetDevice('1.2.3.4', 'admin', 'querty'),
        NetDevice('20.20.20.20', 'admin', 'clackety')
    ]
    
    for my_obj in obj_list:
        print(my_obj.ip_addr)
        print(my_obj.username)
        print(my_obj.password)
        print()


if __name__ == '__main__':
    main()
