a=10
b=20
c=a+b

print ("a:", a, "type:", type(a))
print ("c:", c, "type:", type(c))


#BinaryNumbers
a=0b101
print ("a:",a, "type:",type(a))

b=int("0b101011", 2)
print ("b:",b, "type:",type(b))

#convert
a=43
b=bin(a)
print ("Integer:",a, "Binary equivalent:",b)

#oct
a=int('20',8)
print (a, type(a))

#fgg
a=0O56
print ("a:",a, "type:",type(a))

b=int("0O31",8)
print ("b:",b, "type:",type(b))

c=a+b
print ("addition:", c)

#Additions
a=10 #decimal
b=0b10 #binary
c=0O10 #octal
d=0XA #Hexadecimal
e=a+b+c+d

print ("addition:", e)

#floating point
a=10.33
b=2.66
c=a/b

print ("c:", c, "type", type(c))

