#!/usr/bin/env python3

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def main():

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")

    rd = '100:1'
    vrf = 'blue'

    my_vars = [
        {'ipv4_enabled': True },
        {'ipv4_enabled': False}
    ]


    template_file = 'ex3.j2'
    template = env.get_template(template_file)
    output = template.render(**my_vars, rd, vrf)
    print(output)        



if __name__ == '__main__':
    main()
