import random
import sys
import os

print("Python is here!")

name = "Alwin"
print(name)
name = 15
print(name)

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)
print()
print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)
print()
print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)
print()

quote = "\"Always remember you are Unique!"

multi_line_quote = ''' Just
like everyone else'''

new_string = quote + multi_line_quote

print(quote)
print()
print(multi_line_quote)
print()
print(new_string)
print()
print("%s %s %s" % ('I like the qoute ', quote, multi_line_quote))
print()
print('\n' * 5)
print("I don't like ", end="")
print("new lines")
