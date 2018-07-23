# #summer of code

# #full name greeting
# fname=input("Enter your first name: ")
# mname=input("Enter your middle name: ")
# lname=input("Enter your last name: ")

# print("Hello,"+fname+" "+mname+" "+lname+"! Good day to you.")

# #bigger, better favorite number
# fnumber=input("Tell me your favourite number.\n")
# new_fnumber = str(int(fnumber)+1)
# print("Here is a better number for you, it is"+new_fnumber+", bigger and better.")

# #angry boss
# print("Boss is in a really bad mood.")
# any_answer=input("Hey, what you want?\n")
# yell="whaddaya mean "+"\""+any_answer+"\"?!? you're fired!"
# print(yell.upper())

# #table of contents
# title="Table of Contents"
# chapter="Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13"

# print(title.center(5))
# print(chapter.rjust(10))

#Research how to generate a random number with Python.
import random
# for x in range(10):
#     print(random.randint(1,100))

land = "X"
water ="o"
world = land + water

randstring = ""

for x in range(0, 8):
    randstring += random.choice(world)
print(randstring)

# another method
# string_val = "".join(random.choice(world) for i in range(8))
# print(string_val)

# all possible of combination
# import itertools
# for i in itertools.product(world, repeat=8):
#     print(''.join(i))