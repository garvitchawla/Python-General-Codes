# File Objects

f = open('test.txt', 'r')        # This is the general way to open 'test.txt' file.
# Files are default in 'read' mode = 'r'. Write = 'w'. Append = 'a'. Read and Write = 'r+'

print(f.name)           # test.txt
print(f.mode)           # r


f.close()

# If we open the file in this way which we defined, we have to close the file also, f.close().
# Otherwise, there could end up with leaks that cause you to run over the maximum allowed file descriptors on your system
# and your applications can throw up an error.

# Therefore, it's prefered to use the CONTEXT MANAGER i.e. using the 'with' keyword.
# CONTEXT MANAGERS allow us to manage the file within the block, and after we exit the block of code
# it'll automatically Close the file.
# BENEFIT is we can still use the file object 'f' here outside the block.

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    # If we use f.readlines() instead of f.read(), we can see all the content, even the new line character.
    # We can use f.readline() instead of f.readlines(), readline() will get you just the first line of the file.
    # f.readline() always read the next line, 1 line at a time.
    print(f_contents, end='')       # 1) This is a test file!

    f_contents = f.readline()
    print(f_contents, end='')       # 2) With multiple lines of data...
    # print statement gives a default new line, therefore end = ''

    f_contents = f.read(100)        # 100 means 100 characters. This line will only read NEXT 100 CHARACTERS.
    print(f_contents, end='')

    # But, to see all the lines we can fo readlines()
    # We can also use a for loop on the file object.
    for line in f:
        print(line, end='')         # Prints rest of the lines.

    # If we go further, read() will return an empty string.

    print("\n**********************")

with open('test.txt', 'r') as g:
    # We have to devise a way, through which we can go through the whole file without getting an empty string.
    size_to_read = 10
    g_contents = g.read(size_to_read)
    while len(g_contents) > 0:
        print(g_contents, end='*')
        g_contents = g.read(size_to_read)

print("\n**********************")

with open('test.txt', 'r') as h:
    size_to_read_again = 10
    h_contents = h.read(size_to_read_again)

    print(h.tell())     # tell() will tell the current position of the cursor. 10 character already read.

    # To get our position back to the zero, we can use seek(0) function.

    h_contents = h.read(size_to_read_again)
    h_contents = h.read(size_to_read_again)
    print(h.tell())
    h.seek(0)
    print(h.tell())

    # Through, seek() we can change it to any position in the file.
    # By giving an appropriate number in the seek().


# If you try to write on a file which is open in 'read' mode, it will say 'NOT WRITABLE'.

with open('test2.txt', 'w') as i:
    i.write('Test.')
    # It will create a new file if it doesn't exist or OVER write an old file, so make sure that you write on a new file
    # or use 'a' to append on an existing file.
    i.write('Test Just After That.')
    i.write('It writes back to back.')

    # We can also use seek() here. seek(0) to take it back to 0.
    i.write('Test.')
    i.seek(0)
    i.write('Testing')
    # It overwrite only what it needs to overwrite.
    i.seek(0)
    i.write('R')

# READ from 1 File and WRITE to 2nd File

with open('test.txt', 'r') as rf:       # rf is read file
    with open('test_copy.txt', 'w') as wf:  # wf is write file
        for line in rf:                 # For all the lines in rf.
            wf.write(line)              # Write them to the wf.

# We can also read and write IMAGES, COPY images.
# But, we have to then work with 'binary data' ie Bytes instead of text. As 'utf-8' codec can't decode byte ...
# Therefore change r -> rb and w -> wb.
# FOR IMAGES
'''
with open('test_img.jpg', 'rb') as rf:       # rf is read file
    with open('test_img_copy.jpg', 'wb') as wf:  # wf is write file
        for line in rf:                 # For all the lines in rf.
            wf.write(line)              # Write them to the wf.



# We can also read IMAGES in chunks like we did with text.

with open('test_img.jpg', 'rb') as rf:       # rf is read file
    with open('test_img_copy.jpg', 'wb') as wf:  # wf is write file
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)      # write to the file.
            rf_chunk = rf.read(chunk_size)  # Read more chunk. Otherwise, INFINITE LOOP.
'''