# EXAMPLES OF DATA TYPES:
# boolean/bool: True or False
# int: 1, 2, 10, etc...
# float: 3.14
# string: "katie"
# list: [1, 2, 3] ...an ordered squence of values or other data types...
# dictionary: a collection of key:value pairs {"name": "katie", "age": 35}
# among others... there are more!

# What the heck is dynamic typing!?
# --> it means Python is highly flexible about reassigning variables to different types!
# ex:

awesomeness = True
awesomeness = "dog"
awesomeness = None
awesomeness = 22/7

# The special value None
# None is Python's way of representing 'nothingness' (like 'null' in other languages)

# STRINGS!

# String Escape Characters (they get interpreted by Python to do somethig special)
# some examples -->
# \\ backslash
# \n newline
# \r carriage return
print("hello \n world")

# String Concatenation
str1 = "Hi"
str2 = "silly girl"
str3 = str1 + ", " + str2
print(str3)

# you can also use the += operator!
string1 = "ice"
string1 += " cream"
print(string1)

# String Formatting/Interpolation
# f""
x = 10
formatted = f"I've told you {x} times already!"
print(formatted)

# .format()
y = 11
formatted2 = "I've told you {} times already!".format(11)
print (formatted2)

# % operator(deprecated)
z = 13
formatted3 = "I've told you %d times already!" %(z)
print(formatted3)

# Strings and Indices
ex = "lol"
print(ex[0])

# Converting Data Types
decimal = 12.456789
integer = int(decimal)
print(integer)

my_list = [1, 2, 3]
my_string = str(my_list)
print(my_string)

numbah = 8
string_num = str(numbah)
print(string_num)
