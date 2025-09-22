# LL 6th time and for loops!


import datetime


current = datetime.datetime.now()
hour = current.hour

print(f"the time is: {current}")
print(f"the hour is: {hour}")

#What is a loop? 
# repeating code``
#What are the two types of loops?
# for and while loops
#What is iteration
# repeating
#What are lists? 
# a collection of items


family = ["morgan","parker","lucas"]
print(family[0])
print(family)
family[0] = "morgan"
family[1] = "parker"
family.remove("lucas")
print(family)

# for loop
for sibling in family:
    print(f"hello {sibling}")

for x in range(1,5):
     print(x)

# while loop ∞
#while True:
  #   print("OH NO")

#iterator (keep track of loop)
#

# What is a loop? 
# repeating code
#How do you make lists in python? 
# using square brackets []
#How do you make for loops in python? 
# using for condition:
#How do you make while loops in python?
# using while condition:
#good y loop
i = 1

while i < 21:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 2

import random
    
number = random.randint(1,20)
x = 1
"""while x != number:
    print("duck")
    x += 1

print("goose!!!!!!!!!!!!!!!!!!!!!!!!!")"""

while True:
    if number == x:
        print("Goose!")
        break
    else:
        print("duck")
        x += 1











