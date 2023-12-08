'''
uple is an immutable data type. An immutable object cannot be modified once it is created in the memory.
'''

#tup1 = ("a", "b", "c", "d")
#tup1[2] = 'Z'
#print ("tup1: ", tup1)

'''
How to Update a Python Tuple?
You can use a work-around to update a tuple. Using the list() function, convert the tuple to a list,
perform the desired append/insert/remove operations and then parse the list back to tuple object.
'''

tup1 = ("a", "b", "c", "d")
print ("Tuple before update", tup1, "id(): ", id(tup1))

list1 = list(tup1)
list1[2]='F'
list1.append('Z')
list1.sort()
print ("updated list", list1)

tup1 = tuple(list1)
print ("Tuple after update", tup1, "id(): ", id(tup1))