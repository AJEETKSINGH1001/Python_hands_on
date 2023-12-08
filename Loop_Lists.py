'''
You can traverse the items in a list with Python's for loop construct.
The traversal can be done, using list as an iterator or with the help of index.
'''

lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')

'''
To iterate through the items in a list, 
obtain the range object of integers "0" to "len-1". See the following example −
'''
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])