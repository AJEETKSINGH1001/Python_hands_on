'''
Every computer application should have a provision to accept input from the user
when it is running. This makes the application interactive. Depending on how it is developed, an application may accept the user input in the form of text entered in the console (sys.stdin), a graphical layout, or a web-based interface. In this chapter, we shall learn how Python accepts the user input from the console,
and displays the output also on the same console.

Python User Input Functions
Python provides us with two built-in functions to read the input from the keyboard.

The input () Function
The raw_input () Function
'''

#! /usr/bin/python3.11

name = "Kiran"
city = "Hyderabad"

print ("Hello My name is", name)
print ("I am from", city)

#The input() Function

name = input()
city = input()

print ("Hello My name is", name)
print ("I am from ", city)

#user input

#! /usr/bin/python3.11

name = input("Enter your name : ")
city = input("Enter your city : ")

print ("Hello My name is", name)
print ("I am from ", city)

