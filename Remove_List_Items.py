'''
The list class methods remove() and pop() both can remove an item from a list.
The difference between them is that remove()
removes the object given as argument, while pop() removes an item at the given index.
'''

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)

#Using the pop() Method

list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)

#Using the "del" Keyword
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)

#You can delete a series of consecutive items from a list with the slicing operator.
# Take a look at the following example

list2 = [25.50, True, -55, 1+2j]
print ("List before deleting: ", list2)
del list2[0:2]
print ("List after deleting: ", list2)