'''
word to string
'''

input = "Python is fun"

string = input.split()
first = string[0]
second = string[1]
third = string[2]
fstring = '#' + first.capitalize() + second.capitalize() + third.capitalize()


print(fstring)
