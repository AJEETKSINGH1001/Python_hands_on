'''
There are two methods of the list class, append() and insert(),
that are used to add items to an existing list
'''

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)

#The insert() method inserts the item at a specified index in the list

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list ", list1)

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)

'''
We know that "-1" index points to the last item in the list. 
However, note that, the item at index "-1" in the original list is 69.75. This index is not refreshed after appending 'chemistry'. 
Hence, 'Pass' is not inserted at the updated index "-1", but the previous index "-1".
'''
