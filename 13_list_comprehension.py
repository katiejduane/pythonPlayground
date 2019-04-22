# list comprehension is a powerful way to make new lists! copies of lists, etc...

# syntax
# [___ for ___ in ___]

nums = [1,2,3]
new_nums = [x*10 for x in nums]
print(new_nums)

# it can also be done with a loop, but this is more concise!

name = 'colt'
name_list = [char.upper() for char in name]
print(name_list)

friends = ['sean', 'jason', 'greg']
[friend[0].upper() for friend in friends] # this isn't working for me!
print(friends)

more_nums = [1,2,3,4,5]
string_nums = [str(num) for num in more_nums]
print(string_nums)


# NEED TO FINISH LATER!!!