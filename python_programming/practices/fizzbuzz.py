# LL 6th FizzBuzz


for buzz in range(1,51):
    if buzz % 3 == 0 and buzz % 5 == 0:
        print("FizzBuzz")
    elif buzz % 3 == 0:
        print("Fizz")
    elif buzz % 5 == 0:
        print("Buzz")
    else:
        print(buzz)