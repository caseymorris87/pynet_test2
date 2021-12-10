#!/usr/bin/env python3

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def main():

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")

    interface = 'Ethernet2/1'

    int_vars = [
        {
            'host': 'nxos1',
            'interface': interface,
            'ip_address': '10.1.100.1/24'
        },
        {
            'host': 'nxos2',
            'interface': interface,
            'ip_address': '10.1.100.2/24'
        }
    ] 

    for host in int_vars:
        template_file = 'ex2.j2'
        template = env.get_template(template_file)
        output = template.render(**host)
        print(output)        



if __name__ == '__main__':
    main()
