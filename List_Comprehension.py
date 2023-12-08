'''
List comprehension is a very powerful programming tool. It is similar to set builder notation in mathematics. It is a concise way to create new list by performing some kind of process on each item on existing list.
List comprehension is considerably faster than processing a list by for loop.
'''

chars=[]
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)

squares = [x*x for x in range(1,11)]
print (squares)

#Nested Loops in List Comprehension

list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2]
print (CombLst)

#Condition in List Comprehension

list1=[x for x in range(1,21) if x%2==0]
print (list1)
