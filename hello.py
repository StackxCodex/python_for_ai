from py_compile import main


print("Hello, World!")
age = 38
nickname = "StackxCodex"
#use 3 """ to write a multi-line comment in python"
"""
This is a simple Python program that prints "Hello, World!" to the console. It also defines two variables: 'age' which is set to 38, and 'name' which is set to "StackxCodex". The program demonstrates basic variable assignment and string handling in Python.
""" 
total = age + 10
print("In 10 years, I will be", total, "years old.")


string = "My name is " + nickname + "."

first_name = "Shelly"
last_name = "Rivers"

full_name = first_name + " " + last_name 
print(full_name)

long_dash = "-" * 20
print (long_dash)

len(long_dash)

has_license = True 
can_drive =has_license and age >= 18
print("can I drive?", can_drive)

string = f"Hi, My name is {nickname}!"
print(string)
print(nickname.upper())

temperature = 75
if temperature > 80:
    print("It's hot outside!")
elif temperature < 60:
    print("It's cold outside!")
else:   print("The weather is nice outside!")

