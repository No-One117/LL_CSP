# LL 6th Old Enough

age = int(input("Enter your age: "))

if age >=21:
    print("your old enough to drink the fun juice")
elif age >= 18:
    print("You are old enough to vote, but not drink the fun juice")
elif age >= 16:
    print("You are old enough to drive, but not old enough to vote.")
elif age >= 15:
    print("You are old enough to get a learner's permit, but not a drivers license nor vote.")
elif age >= 5:
    print("You are old enough to go to school, but not old enough to have a learners permit, vote or drive")
else:
    print("You are not old enough for school, a permit, driving, or voting.")
