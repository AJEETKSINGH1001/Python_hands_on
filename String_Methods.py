'''
Python's built-in str class defines different methods. They help in manipulating strings. Since string is an immutable object, these methods return a copy of the original string, performing the respective processing on it.

The string methods can be classified in following categories −

Case conversion

Alignment

Split and join

Boolean

Find and replace

Formatting

Translate

'''

mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"
count=0
for x in mystr:
   if x.lower() in vowels: count+=1
print ("Number of Vowels:", count)


mystr = '10101'

def strtoint(mystr):
   for x in mystr:
      if x not in '01': return "Error. String with non-binary characters"
   num = int(mystr, 2)
   return num
print ("binary:{} integer: {}".format(mystr,strtoint(mystr)))