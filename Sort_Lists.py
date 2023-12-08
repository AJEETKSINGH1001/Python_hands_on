'''
The sort() method of list class rearranges the items in ascending or descending order with the use of
lexicographical ordering mechanism. The sorting is in-place, in the sense the rearrangement takes place in the same list object,
and that it doesn't return a new object.
'''

list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort", list1)
list1.sort()
print ("list after sort : ", list1)

print ("Descending sort")

list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)

###################################################

list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list1)
list1.sort(key=str.lower)
print ("list after sort : ", list1)

#use a user-defined function as the key parameter in sort()

def myfunction(x):
   return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)