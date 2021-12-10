import os
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config



device_dict = {'host':'srx2.lasthop.io', 'user':'pyclass', 'password': getpass()}

jun_dev = Device(**device_dict)

jun_dev.open()

jun_dev.timeout=80

cfg = Config(jun_dev)

cfg.lock()

try:
    cfg.lock()
except LockError as e:
    print (e)

cfg.load('set system host-name some-stuff', format='set', merge=True)

print(cfg.diff())

cfg.rollback(0)

print(cfg.diff())

cfg.unlock()






