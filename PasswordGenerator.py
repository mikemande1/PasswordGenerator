import random

# List of Characters to be used in the passworsd
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':\"<>,.?/~`"

while True:
    try:
        length = int(
            input("How many characters would you like in your password?"))
        break
    except ValueError:
        print("That is not a valid number. Please try Again.")


# use the random module to generate a password by selecting random characters from the character list
password = ""
for i in range(length):
    password += random.choice(characters)


# print the generated password
print(password)
