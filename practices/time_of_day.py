import datetime

current = datetime.datetime.now()
hour = current.hour

print(f"The time is: {current}")
print(f"The hour is: {hour}")

if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")

