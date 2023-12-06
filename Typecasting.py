'''
In Python there are different data types, such as numbers, sequences, mappings etc.
There may be a situation where, you have the available data of one type but you want to use it in another form. For example, the user has input a string but you want to use it as a number.
Python's type casting mechanism let you do that.

Python Type Casting is a process in which we convert a literal of one data type to another data type.
Python supports two types of casting − implicit and explicit.

In implicit type casting, a Python object with lesser byte size is upgraded to match the bigger byte size of
other object in the operation. For example, a Boolean object is first upgraded to int and then to float, before the addition with a floating point object. In the following example, we try to add a Boolean object in a float,
please note that True is equal to 1, and False is equal to 0.
'''

a=True;
b=10.5;
c=a+b;

print (c);


