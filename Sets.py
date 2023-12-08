'''
Set in Python also a collection data type such as list or tuple. However,
it is not an ordered collection, i.e., items in a set or not accessible by its positional index.
A set object is a collection of one or more immutable objects enclosed within curly brackets {}.
'''

s1 = {"Rohan", "Physics", 21, 69.75}
s2 = {1, 2, 3, 4, 5}
s3 = {"a", "b", "c", "d"}
s4 = {25.50, True, -55, 1+2j}
print (s1)
print (s2)
print (s3)
print (s4)

'''
set() Function
set() is one of the built-in functions. 
It takes any sequence object (list, tuple or string) as argument and returns a set object
'''

#The set() function returns a set object from the sequence, discarding the repeated elements in it.

L1 = ["Rohan", "Physics", 21, 69.75]
s1 = set(L1)
T1 = (1, 2, 3, 4, 5)
s2 = set(T1)
string = "TutorialsPoint"
s3 = set(string)

print (s1)
print (s2)
print (s3)

#Set is a collection of distinct objects. Even if you repeat an object in the collection,
# only one copy is retained in it.

s2 = {1, 2, 3, 4, 5, 3,0, 1, 9}
s3 = {"a", "b", "c", "d", "b", "e", "a"}
print (s2)
print (s3)

'''
Only immutable objects can be used to form a set object. 
Any number type, string and tuple is allowed, 
but you cannot put a list or a dictionary in a set.
'''
s1 = {1, 2, [3, 4, 5], 3,0, 1, 9}
print (s1)
s2 = {"Rohan", {"phy":50}}
print (s2)


