def file_opener(file_name):
    with open(file_name) as f:
        return f.read()

def find_vendor(data_lines):
    return data_lines[0].split()[0]

def find_model(data_lines):
    return data_lines[31].split()[1]

def find_version(data_lines):
    return data_lines[0].split()[7].rstrip(',')

def find_serial(data_lines):
    return data_lines[32].split('Processor board ID')[1]

def find_uptime(data_lines):
    return data_lines[7].split('is')[1].strip()

file_data = file_opener('show_version.txt').splitlines()

print(
    find_vendor(file_data), 
    find_model(file_data), 
    find_version(file_data), 
    find_serial(file_data),
    find_uptime(file_data))
 
        
