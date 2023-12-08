T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = T1+T2
print ("Joined Tuple:", T3)

#ex2

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T1+=T2
print ("Joined Tuple:", T1)

#Using extend function

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)

#using sum function

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Joined Tuple using sum function:", T3)

#joining tuple using for loop

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1, L2 = list(T1), list(T2)
L3 = [y for x in [L1, L2] for y in x]
T3 = tuple(L3)
print ("Joined Tuple using for loop:", T3)

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
   T1+=(t,)
print (T1)