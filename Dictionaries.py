'''
Dictionary is one of the built-in data types in Python. Python's dictionary is example of mapping type.
A mapping object 'maps' value of one object with another.
In a language dictionary we have pairs of word and corresponding meaning.
Two parts of pair are key (word) and value (meaning). Similarly, Python dictionary is also a collection of key:value pairs.
The pairs are separated by comma and put inside curly brackets {}.
'''

#Only a number, string or tuple can be used as key. All of them are immutable.
# You can use an object of any type as the value. Hence following definitions of dictionary are also valid −
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

#Python doesn't accept mutable objects such as list as key, and raises TypeError.

#d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}
#print (d1)

#You can assign a value to more than one keys in a dictionary,
# but a key cannot appear more than once in a dictionary.

d1 = {"Banana":"Fruit", "Rose":"Flower", "Lotus":"Flower", "Mango":"Fruit"}
d2 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus"}
print (d1)
print (d2)

'''
Python Dictionary Operators
Operator	Description	Example
dict[key]	Extract/assign the value mapped with key	print (d1['b']) retrieves 4
d1['b'] = 'Z' assigns new value to key 'b'

dict1|dict2	Union of two dictionary objects, retuning new object	d3=d1|d2 ; print (d3)
{'a': 2, 'b': 4, 'c': 30, 'a1': 20, 'b1': 40, 'c1': 60}

dict1|=dict2	Augmented dictionary union operator	d1|=d2; print (d1)
{'a': 2, 'b': 4, 'c': 30, 'a1': 20, 'b1': 40, 'c1': 60}
A dictionary in Python is not a sequence, as the elements in dictionary are not indexed. Still, 
you can use the square brackets. 
"[ ]" operator to fetch the value associated with a certain key in the dictionary object.
'''

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])

#Python raises a KeyError if the key given inside the square brackets is not present in the dictionary object.

#capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
#print ("Captial of Haryana is : ", capitals['Haryana'])

#Using the get() Method

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))
print ("Capital of Karnataka is: ", capitals.get('Karnataka'))

#Unlike the "[]" operator, the get() method doesn't raise error if the key is not found; it return None.

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana'))

#The get() method accepts an optional string argument. If it is given, and if the key is not found, this string becomes the return value.

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana', 'Not found'))



