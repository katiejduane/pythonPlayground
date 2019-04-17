







# the 'try' keyword:
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
