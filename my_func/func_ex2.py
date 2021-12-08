
def my_func(five, six, seven):
  print(five, six, seven)

my_list = [5, 6, 7]
my_func(*my_list)

my_dict = {'five': 5, 'six': 6, 'seven': 7}
my_func(**my_dict)

