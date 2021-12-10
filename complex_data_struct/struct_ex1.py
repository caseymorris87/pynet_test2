#!/usr/bin/env python3

import json
from rich import print


def file_opener(filename):

    with open(filename) as f:
        return f.read()

def data_parser(json_data):

    parsed_data = {}

    for e in json_data:
        if e['protocol'] != 'L':
            new_dict = {}
            new_dict['nexthop_interface'] = e['nexthop_if']
            new_dict['nexthop_ip'] = e['nexthop_ip']
            parsed_data[e['network']] = new_dict

    return parsed_data

def main():
    
    file_data = file_opener('struct_data1.json')
   
    json_data = json.loads(file_data)
    
    print(json_data)
    print()
    print()
    print(type(json_data))
    print(len(json_data))
    print()
    print(type(json_data[0]))
    print(len(json_data[0]))
    
    parsed_data = data_parser(json_data)

    print()
    print()
    print(parsed_data)

    
    
        


if __name__ == '__main__':
    main()
