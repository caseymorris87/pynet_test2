def my_func(x, y, z=20):
  return x + y + z

print(my_func(10, 10, 20))
print(my_func(x=10, y=10))
print(my_func(10, z=30, y=20))
print(my_func(z='one', x='two', y='three'))
print(my_func(['stuff'], ['to'], ['do']))

