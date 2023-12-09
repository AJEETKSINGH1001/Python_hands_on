'''
file_name − The file_name argument is a string value that contains the name of the file that you want to access.
access_mode − The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc.
This is an optional parameter and the default file access mode is read (r).
'''

# Open a file
fo = open("foo.txt", "r")
text = fo.read()
print (text)

# Close the opened file
fo.close()

#Reading in Binary Mode

f=open('test.bin', 'wb')
data=b"Hello World"
f.write(data)
f.close()

# Open a file in read-write mode
fo=open("foo.txt","w+")
fo.write("This is a rat race")
fo.seek(10,0)
data=fo.read(3)
fo.seek(10,0)
fo.write('cat')
fo.seek(0,0)
data=fo.read()
print (data)
fo.close()