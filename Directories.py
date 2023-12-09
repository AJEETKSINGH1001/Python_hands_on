#The mkdir() Method
#!/usr/bin/python3
import os

# Create a directory "test"
os.mkdir("test")

'''
A file object is created using open() function. The file class defines the following methods with which different file IO operations can be done. The methods can be used with any file like object such as byte stream or network stream.

Sr.No.	Methods & Description
1	
file.close()

Close the file. A closed file cannot be read or written any more.

2	
file.flush()

Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.

3	
file_fileno()

Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.

4	
file.isatty()

Returns True if the file is connected to a tty(-like) device, else False.

5	
next(file)

Returns the next line from the file each time it is being called.

6	
file.read([size])

Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).

7	
file.readline([size])

Reads one entire line from the file. A trailing newline character is kept in the string.

8	
file.readlines([sizehint])

Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

9	
file.seek(offset[, whence])

Sets the file's current position

10	
file.tell()

Returns the file's current position

11	
file.truncate([size])

Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.

12	
file.write(str)

Writes a string to the file. There is no return value.

13	
file.writelines(sequence)
Writes a sequence of strings to the file. 
The sequence can be any iterable object producing strings, typically a list of strings.

The os module provides a big range of useful methods to manipulate files. Most of the useful methods are listed here −

Sr.No.	Methods with Description
1

os.close(fd)

Close file descriptor fd.

2

os.closerange(fd_low, fd_high)

Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.

3

os.dup(fd)

Return a duplicate of file descriptor fd.

4

os.fdatasync(fd)

Force write of file with filedescriptor fd to disk.

5

os.fdopen(fd[, mode[, bufsize]])

Return an open file object connected to the file descriptor fd.

6

os.fsync(fd)

Force write of file with filedescriptor fd to disk.

7

os.ftruncate(fd, length)

Truncate the file corresponding to file descriptor fd, so that it is at most length bytes in size.

8

os.lseek(fd, pos, how)

Set the current position of file descriptor fd to position pos, modified by how.

9

os.open(file, flags[, mode])

Open the file file and set various flags according to flags and possibly its mode according to mode.

10

os.read(fd, n)

Read at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned.

11

os.tmpfile()

Return a new file object opened in update mode (w+b).

12

os.write(fd, str)

Write the string str to file descriptor fd. Return the number of bytes actually written.

'''



