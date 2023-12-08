'''
its items cannot be accessed individually as they do not have a positional index (as in list or tuple). Set items do not have a key either (as in dictionary) to access.
You can only traverse the set items using a for loop.
'''

langs = {"C", "C++", "Java", "Python"}
for lang in langs:
   print (lang)


'''
Python's membership operators let you check if a certain item is available in the set. 
Take a look at the following example
'''

langs = {"C", "C++", "Java", "Python"}
print ("PHP" in langs)
print ("Java" in langs)