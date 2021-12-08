def file_opener(my_file):
  with open(my_file) as f:
    output = f.read()
    return output

def output_parse(output):
  output = output.splitlines()
  for line in output:
    if 'Processor board ID' in line: #can also split by this string to get a two elem list. one being empty, other having the serial
      serial = line.split()[3]
  return serial

file_string = file_opener('show_version.txt')
serial_num = output_parse(file_string)

print(serial_num)
     

