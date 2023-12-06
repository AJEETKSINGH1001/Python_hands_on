'''
Python logical operators are used to form compound Boolean expressions.
Each operand for these logical operators is itself a Boolean expression.
'''

x = 10
y = 20
print("x > 0 and x < 10:",x > 0 and x < 10)
print("x > 0 and y > 10:",x > 0 and y > 10)
print("x > 10 or y > 10:",x > 10 or y > 10)
print("x%2 == 0 and y%2 == 0:",x%2 == 0 and y%2 == 0)
print ("not (x+y>15):", not (x+y)>15)

#logiv

x = 10
y = 20
z = 0
print("x and y:",x and y)
print("x or y:",x or y)
print("z or x:",z or x)
print("y or z:", y or z)

#tuple
a="Hello"
b=tuple()
print("a and b:",a and b)
print("b or a:",b or a)

'''
a="Hello"
b=tuple()
print("a and b:",a and b)
print("b or a:",b or a)
'''

x=[1,2,3]
y=[10,20,30]
print("x and y:",x and y)
print("x or y:",x or y)