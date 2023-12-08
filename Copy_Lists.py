'''
In Python, a variable is just a label or reference to the object in the memory. Hence, the assignment "lst1 = lst" refers
to the same list object in the memory
'''

lst = [10, 20]
print ("lst:", lst, "id(lst):",id(lst))
lst1 = lst
print ("lst1:", lst1, "id(lst1):",id(lst1))

# if we update "lst", it will automatically reflect in "lst1". Change lst[0] to 100

lst[0]=100
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))

#Copy Method of List Class

lst = [10, 20]
lst1 = lst.copy()
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))




