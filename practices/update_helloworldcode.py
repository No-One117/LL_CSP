# Define a function that prints a hello message
def sayHello(name):
    print("Hello, " + name + "!")

# Repeat the following steps 5 times
count = 1
while count <= 5:
    # Ask the user to enter a name
    name = input("Enter name " + str(count) + ": ")

    # Call the function to say hello
    sayHello(name)

    # Increase the count by 1
    count = count + 1



