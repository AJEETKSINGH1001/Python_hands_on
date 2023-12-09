'''
The "[]" operator (used to access value mapped to a dictionary key)
is used to update an existing key-value pair as well as add a new pair.
'''

#dict["key"] = val

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: ", marks)
marks['Laxman'] = 95
print ("marks dictionary after update: ", marks)

#However, an item with 'Krishnan' as its key is not available in the dictionary,
# hence a new key-value pair is added.

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: ", marks)
marks['Krishan'] = 74
print ("marks dictionary after update: ", marks)

#Using the update() Method d1.update(d2)

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks.update(marks1)
print ("marks dictionary after update: \n", marks)

#Update with Iterable
#d1.update([(k1, v1), (k2, v2)])

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = [("Sharad", 51), ("Mushtaq", 61), ("Laxman", 89)]
marks.update(marks1)
print ("marks dictionary after update: \n", marks)

#Update with Keyword Arguments

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks.update(Sharad = 51, Mushtaq = 61, Laxman = 89)
print ("marks dictionary after update: \n", marks)

#Using the Unpack Operator
#The "**" symbol prefixed to a dictionary object unpacks it to a list of tuples, each tuple with key and value.

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)

#Using the Union Operator (|)
'''
Python introduces the "|" (pipe symbol) as the union operator for dictionary operands. 
It updates existing keys in dict object on left, and adds new key-value pairs to return a new dict object.
'''

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)

'''
Using "|=" Operator
The "|=" operator is an augmented Union operator. 
It performs in-place update o n the dictionary operand on left by adding new keys in the operand on right, 
and updating the existing keys.
'''
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("marks dictionary after update: \n", marks)


