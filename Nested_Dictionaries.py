'''
A Python dictionary is said to have a nested structure if value of one or more keys is another dictionary.
A nested dictionary is usually employed to store a complex data structure.
'''

marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}

marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}
for k,v in marklist.items():
   print (k, ":", v)


