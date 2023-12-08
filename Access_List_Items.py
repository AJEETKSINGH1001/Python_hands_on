'''
In Python, a list is a sequence. Each object in the list is accessible with its index. The index starts from 0.
Index or the last item in the list is "length-1". To access the values in a list,
use the square brackets for slicing along with the index or indices to obtain value available at that index.
'''

list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]

print ("Item at 0th index in list1: ", list1[0])
print ("Item at index 2 in list2: ", list2[2])

#Python allows negative index to be used with any sequence type.
# The "-1" index refers to the last item in the list.

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Item at 0th index in list1: ", list1[-1])
print ("Item at index 2 in list2: ", list2[-3])

'''
i − index of the first item in the sublist

j − index of the item next to the last in the sublist
'''

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Items from index 1 to 2 in list1: ", list1[1:3])
print ("Items from index 0 to 1 in list2: ", list2[0:2])

#

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list4 = ["Rohan", "Physics", 21, 69.75]
list3 = [1, 2, 3, 4, 5]

print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 2 to last in list3", list3[2:-1])
print ("Items from index 0 to index last in list4", list4[:])