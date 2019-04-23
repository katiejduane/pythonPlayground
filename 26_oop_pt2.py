# OOP part two! --------------------------------------->

# Inheritance!
# A key feature of OOP is the ability to define a class which 
# inherits from another class (aka a 'parent' class)

# In python, inheritance works by apssing the parent class as 
# an argument to the definition of a child class

# class Animal:
#     cool = True
#     def make_sound(self,sound):
#         print(f"this animal says {sound}")

# class Cat(Animal):
#     pass

# blue = Cat()
# blue.make_sound('meeeoooowwww')

# All about PROPERTIES! ---------------------------------->

class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property # decorator for property
    # above is syntax for a 'getter'
    def age(self):
        return self._age
        # this method allows you to print just 'jane.age'

    @age.setter
    # above is the syntax for a 'setter'
    def age(self, value):
            if value >= 0:
                self._age = value
            else:
                raise  ValueError("age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

jane = Human("jane","goodall",70)
# print(jane.get_age())
# jane.set_age(55)
# print(jane.get_age())
# print(jane.age)
# jane.age = 45
# print(jane.age)
# print(jane.full_name)


# Introduction to SUPER() ---------------------------------->

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")

    def __str__(self):
        return f"{self.name} is a bad {self.species}"
        #what is the real difference between str and repr? can i target one vs the other?
    


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super() .__init__(name, species="cat")
        # this refers to the PARENT CLASS (in this case, Animal)
        self.breed = breed
        self.toy = toy
    def play(self):
        print(f"{self.name} plays with {self.toy}")
    

blue = Cat('blue', 'scottish fold', 'string')
blue.make_sound('meeeoooowwww')

print(blue.toy)
blue.play()
print(blue.__repr__())
print(blue.__str__())

