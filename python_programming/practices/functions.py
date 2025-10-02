# LL 6th Function Notes

#what a function is

#a function is a set of instructions that are executed
# they can be used for anything

name = input("what is your name")

print(f"hello {name}")

def add():
    print(num_one + num_two)

num_one = 14
num_two = 12

add()

#Why we use functions

#Modularize code: Break down complex problems into smaller, manageable parts

#How to write a function in Python\

def greet(name):
    print(f"Hello, {name}!")

#What parameters and arguments are

#Arguments are when we call the function and parameters are when we define the function

#How to use parameters and arguments in python

def add_numbers(num1, num2): # num1 and num2 are parameters
    return num1 + num2

result = add_numbers(5, 3) # 5 and 3 are arguments
print(result) # Output: 8

#What return statements are

#A return statement is used within a function to send a value back to the caller.

#How to use return statements in a program

def multiply(a, b):
    product = a * b
    return product # Returns the calculated product

value = multiply(4, 6)
print(value) # Output: 24

#indents must always match (for functions)

def clean(info):
    return info.strip().lower()

name  = input("What is your name")
quest  = input("What is your quest")
wingspeed  = input("What is the average wind velocity of an unladen swallow ")

print(f"hello, {clean(name)} i have been trying to contact you about your cars extended warrenty no i dont care about you g{clean(quest)}, why did you tell me that the average wing speed of an unladen swallow is {clean(wingspeed)} i dont care ")

#believe("why do people like skibidi toilet?")
