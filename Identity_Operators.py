'''
Python has two identity operators is and is not. Both return opposite Boolean values. The "in" operator evaluates to True if both the operand objects share the same memory location. The memory location of the object can be obtained by the "id()" function. If the id() of both variables is same,
the "in" operator returns True (as a consequence, is not returns False).
'''

a="TutorialsPoint"
b=a
print ("id(a), id(b):", id(a), id(b))
print ("a is b:", a is b)
print ("b is not a:", b is not a)

#list and tuple

a=[1,2,3]
b=[1,2,3]
print ("id(a), id(b):", id(a), id(b))
print ("a is b:", a is b)
print ("b is not a:", b is not a)