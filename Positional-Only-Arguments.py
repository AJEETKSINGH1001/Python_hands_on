'''
It is possible to define a function in which one or more arguments can not accept their value with keywords.
Such arguments may be called positional-only arguments.
Python's built-in input() function is an example of positional-only arguments.
The syntax of input function is −
'''

def intr(amt, rate, /):
   val = amt*rate/100
   return val

name = input("enter your name ")

def myfunction(a,b,c):
 myfunction(10, y=20, z=30)
 myfunction(10, 20, z=30)