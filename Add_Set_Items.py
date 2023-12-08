#add() Method
lang1 = {"C", "C++", "Java", "Python"}
lang1.add("Golang")
print (lang1)

#update() Method
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print (lang1)

#The update() method also accepts any sequence object as argument.
#Here, a tuple is the argument for update() method.

lang1 = {"C", "C++", "Java", "Python"}
lang2 = ("PHP", "C#", "Perl")
lang1.update(lang2)
print (lang1)

set1 = set("Hello")
set1.update("World")
print (set1)

'''
The union() method of set class also combines the unique items from two sets, 
but it returns a new set object.
'''

lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = lang1.union(lang2)
print (lang3)

lang1 = {"C", "C++", "Java", "Python"}
lang2 = ["PHP", "C#", "Perl"]
lang3 = lang1.union(lang2)
print (lang3)