'''
The raw_input() function works similar to input() function.
Here only point is that this function was available in Python 2.7, and it has been renamed to input() in Python 3.6

Following is the syntax of the raw_input() function:

'''

#! /usr/bin/python3.11

def raw_input(param):
    pass


name = raw_input("Eneter your name - ")
city = raw_input("Enter city name - ")

print ("Hello My name is", name)
print ("I am from ", city)

#Taking Numeric Input

'''
Why do you get a TypeError here? The reason is, Python always read the user input as a string. 
Hence, width="20" and height="30" are the strings and obviously you cannot perform multiplication of two strings.
To overcome this problem, we shall use int(), another built-in function from Python's 
standard library. It converts a string object to an integer.
'''
#! /usr/bin/python3.11

width = int(input("Enter width : "))
height = int(input("Enter height : "))

area = width*height
print ("Area of rectangle = ", area)

#Python's float() function converts a string into a float object
#! /usr/bin/python3.11

amount = float(input("Enter Amount : "))
rate = float(input("Enter rate of interest : "))

interest = amount*rate/100
print ("Amount: ", amount, "Interest: ", interest)




