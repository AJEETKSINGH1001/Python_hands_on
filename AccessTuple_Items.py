tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)

print ("Item at 0th index in tup1tup2: ", tup1[0])
print ("Item at index 2 in list2: ", tup2[2])

#Python allows negative index to be used with any sequence type.
# The "-1" index refers to the last item in the tuple.
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)
print ("Item at 0th index in tup1: ", tup1[-1])
print ("Item at index 2 in tup2: ", tup2[-3])

#Extracting a Subtuple from a Tuple
#Parameters
#i − index of the first item in the subtup

#j − index of the item next to the last in the subtup

tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)

print ("Items from index 1 to 2 in tup1: ", tup1[1:3])
print ("Items from index 0 to 1 in tup2: ", tup2[0:2])

#ex
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)
tup4 = ("Rohan", "Physics", 21, 69.75)
tup3 = (1, 2, 3, 4, 5)

print ("Items from index 1 to last in tup1: ", tup1[1:])
print ("Items from index 0 to 1 in tup2: ", tup2[:2])
print ("Items from index 2 to last in tup3", tup3[2:-1])
print ("Items from index 0 to index last in tup4", tup4[:])