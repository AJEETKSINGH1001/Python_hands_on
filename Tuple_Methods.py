'''
Since a tuple in Python is immutable,

the tuple class doesn't define methods for adding or removing items. The tuple class defines only two methods.
1
tuple.count(obj)

Returns count of how many times obj occurs in tuple

2	tuple.index(obj)
Returns the lowest index in tuple that obj appears
'''

#The index() method returns an integer, representing the index of the first occurrence of "obj"

tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
print ("First index of 10:", x)

#Counting Tuple Items

tup1 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(10)
print ("count of 10:", c)

#tupple count

Tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print ("Tup1:", tup1)
c1 = tup1.count(0.25)
print ("count of 10:", c1)
