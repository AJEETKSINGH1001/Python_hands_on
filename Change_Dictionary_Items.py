'''
Apart from the literal representation of dictionary, where we put comma-separated key:value pairs in curly brackets,
we can create dictionary object with built-in dict() function.
'''

d1 = dict()
d2 = {}
print ('d1: ', d1)
print ('d2: ', d2)

#Dictionary from List of Tuples

d1=dict([('a', 100), ('b', 200)])
d2 = dict((('a', 'one'), ('b', 'two')))
print ('d1: ', d1)
print ('d2: ', d2)

#

d1=dict(a= 100, b=200)

d2 = dict(a='one', b='two')
print ('d1: ', d1)
print ('d2: ', d2)