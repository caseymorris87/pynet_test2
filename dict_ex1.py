my_dev = {'ip_address': '10.10.10.10', 'username': 'admin', 'password': 'pass123', 'vendor': 'cisco', 'model': '9556'}

for k,v in my_dev.items():
  print(k, v)

my_dev['password'] = 'new_pass'

print(my_dev)

my_dev['secret'] = 'some_val'

print(my_dev.get('device_type', 'cisco_ios'))
