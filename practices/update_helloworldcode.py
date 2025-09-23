def say_hello(name):

  print(f"Hello, {name}!")


for i in range(5):
  user_name = input(f"Enter name {i+1}: ")
  say_hello(user_name)


