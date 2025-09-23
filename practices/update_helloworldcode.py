def say_hello(name):
  """Prints a greeting message to the given name."""
  print(f"Hello, {name}!")

# Call the function 5 times with different names from user input
for i in range(5):
  user_name = input(f"Enter name {i+1}: ")
  say_hello(user_name)


