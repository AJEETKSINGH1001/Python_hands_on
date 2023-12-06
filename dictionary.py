'''
Python dictionary is like associative arrays or hashes found in Perl and consist of key:value pairs.
The pairs are separated by comma and put inside curly brackets {}.
To establish mapping between key and value, the semicolon':' symbol is put between the two.

In Python, dictionary is an object of the built-in dict class.
We can check it with the type() function.
Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).
For example
'''



dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values