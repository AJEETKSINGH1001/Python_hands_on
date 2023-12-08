'''
List is a mutable data type in Python. It means, the contents of list can be modified in place, after the object is stored in the memory.
You can assign a new value at a given index position in the list
'''

list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print ("List after changing value at index 2: ", list3)

#In the following code, items at index 1 and 2 are replaced by items in another sublist.

list1 = ["a", "b", "c", "d"]

print ("Original list: ", list1)

list2 = ['Y', 'Z']
list1[1:3] = list2

print ("List after changing with sublist: ", list1)

#If the source sublist has more items than the slice to be replaced,
# the extra items in the source will be inserted. Take a look at the following code.

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

#If the sublist with which a slice of original list is to be replaced, has lesser items,
# the items with match will be replaced and rest of the items in original list will be removed.

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)