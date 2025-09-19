# Define a function that prints a hello message
def sayHello(name):
    print("Hello, " + name ")

# Repeat the steps 5 times using a for loop
for count in range(1, 6):
    # Ask the user to enter a name
    name = input("Enter name " + str(count) + ": ")

    # Call the function to say hello
    sayHello(name)
