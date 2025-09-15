#LL 6th name_decorator.py

# Prompt the user for their name and store it in a variable
user_name = input("Please enter your name: ")

# Define several decorative options
decoration1 = "<<< "
decoration2 = "--- "
decoration3 = ":) :) "

# Concatenate the decorations with the user's name
decorated_name_option1 = decoration1 + user_name + " >>>"
decorated_name_option2 = decoration2 + user_name + " ---"
decorated_name_option3 = decoration3 + user_name + " :) :)"

# Print the different decorated name options
print("Here are your name decoration options:")
print(decorated_name_option1)
print(decorated_name_option2)
print(decorated_name_option3)
