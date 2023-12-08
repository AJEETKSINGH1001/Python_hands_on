'''
In Python, List is classified as a sequence type object. It is a collection of items,
which may be of different data types, with each item having a positional index starting with 0
'''

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L3 = L1+L2
print ("Joined list:", L3)

#augmented concatenation operator with "+=" symbol to append L2 to L1

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1+=L2
print ("Agumented Joined list:", L1)

#same result can be obtained by using the extend() method.

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1.extend(L2)
print ("Joined list:", L1)

#Traverse items of second list with a for loop, and append each item in the first
L1 = [10, 20, 30, 40]
L2 = ['one', 'two', 'three', 'four']

for x in L2:
    L1.append(x)

print("Joined list:", L1)


