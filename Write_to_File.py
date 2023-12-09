'''
To write data to a file in Python, you need to open a file.
Any object that interacts with input and output steam is called File object.
Python's built-in function open() returns a file object.
'''

#fileObject = open(file_name [, access_mode][, buffering])

# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opened file
fo.close()

f=open('test.bin', 'wb')
data=b"Hello World"
f.write(data)
f.close()

#Appending to a File
# Open a file in append mode
fo = open("foo.txt", "a")
text = "this is good Python tutorial"
fo.write(text)

# Close opened file
fo.close()

# Open a file in read-write mode
fo=open("foo2.txt","w+")
fo.write("This is a rat race")
fo.seek(10,0)
data=fo.read(3)
fo.seek(10,0)
fo.write('cat')
fo.close()