# Define OOP, understand encapsulation and abstraction, create classes and instances 
# and attach methods/properties to each!

# OOP: using code to represent or recreate things that exist in the world (a car, a user, a card,
# etc...) but not in code! it uses classes and objects to do this!

# CLASS: blueprints (recipes) for objets. they contain methods (functions) and attributes
# (similar to keys in a dictionary)

# OBJECT: an "instance" of a class. they contain their class's methods and properties.

# Encapsulation: the goal with OOP is the ecnapsulate our code into a logical hierarchical
# groupings using classes. The goruping of public and private attributes and methods into a
# programmatic class, making abstraction possible. Think of it as a little bubble; we want
# the fewest entries and exits into and out of that bubble as possible

# Abstraction: Exposing only the relevant data in a class interface, hiding private attibutes
# and methods (aka the 'inner workings') from users; simple hiding the complex. We abstract it!


# CREATING classes and intances! ----------------------------------------------->

# class naming: upper case first letter, but then camel case to follow, in the singular!
# class User:
#     # python will always look for the INIT method whenever we make a new class!
#     def __init__(self, first, last, age):
#         # self has to go there! it refers to each individual instance of a class!
#         # it must be the first paramater to not only __init__ but to any methods and
#         # properties on class instances!
#         self.first = first
#         self.last = last
#         self.age = age
#         self.__secret = "i like turtles!"

# #creating an objectthat is an instance of a class is called INSTANTIATING a class
# user1 = User('Bianca', 'LaBonita', 37)
# print(user1.first, user1.last)

# dunder methods, name mangling, and more! ----------------------------------------------->
# __name__ (two underscores before and after)
# these are special methods in python, don't go out and make your own dunder methods!

# __twoUnderscores: this actually does something behind the scenes (unlike _oneUnderScore).
# python is "mangling" the name that comes after two underscores. In order to access the data
# when something is named like this, you must do: print(user1_User__secret). Itmakes it PARTICULAR
# to this class, not necessarily to anything that inherits from this class.

# Adding Instance Methods! ----------------------------------------------->
# Special functions for each instance of a class! This is what really separates objects from dicts.

# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.__secret = "i like turtles!"

# # what would we actually put in a method? it depends on the class and what it needs to do.
#     def full_name(self):
#         # still need to provide self (first param)! because it references every unique instance of a class
#         return f"{self.first} {self.last}"
#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}."
#     def likes(self, thing):
#         return f"{self.first} likes {thing}."
#     def is_senior(self):
#         return self.age >= 65
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th birthday, {self.first}!"

# user1 = User('Bianca', 'LaBonita', 37)
# print(user1.full_name())
# print(user1.initials())
# print(user1.likes('lizards'))
# print(user1.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

# Classes/objects aren't just storage places for data (like dicts), they also have functionality!

# Introducing class attributes! ----------------------------------------------->
# class attributes are defined ONCE, and live on the class itself. They are shared by all instances
# of that class in the various objects made from it! They're less common than instance attributes

class User:
    active_users = 0 # this is a class attribute!
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.__secret = "i like turtles!"
        User.active_users += 1
        # anytime a new user is created, __init__ runs and this line adds another active user!
    
    def logout(self):
        User.active_users -= 1
        # this instance method decrements the class attribute active_users ANYTIME a user logs out!
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    def likes(self, thing):
        return f"{self.first} likes {thing}."
    def is_senior(self):
        return self.age >= 65
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}!"


print(User.active_users) # note i am referring to the class itself and not an instance of it!
user1 = User('Bianca', 'LaBonita', 37)
print(User.active_users)
