'''
items in a tuple with Python's for loop construct. The traversal can be done,
using tuple as an iterator or with the help of index.
'''

tup1 = (25, 12, 10, -21, 10, 100)
for num in tup1:
   print (num, end = ' ')


#Indices

tup1 = (25, 12, 10, -21, 10, 100)
indices = range(len(tup1))
for i in indices:
   print ("tup1[{}]: ".format(i), tup1[i])