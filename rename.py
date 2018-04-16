import os

os.chdir('/Users/garvitchawla/PycharmProjects/NokiaInterview/RenameFolder ')
print(os.getcwd())

for f in os.listdir():
    # print(f)                            # Display all files in the directory.
    # print(os.path.splitext(f))          # It will split Name and the Extension.
    # It will give you 2 Values.
    # 1 is Name and 2nd is Extension.
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))
    f_title, f_title2, f_no = file_name.split('-')
    print(f_no)

    # It will have an extra space. So we need to strip() those variables. # Strip away any White spaces.
    f_title = f_title.strip()
    f_no = f_no.strip()
    f_title2 = f_title2.strip()

    # If we dont want the pound sign or the '#', we can take everything from the 2nd variable.
    f_title = f_title.strip()[1:]
    f_no = f_no.strip()[1:]
    f_title2 = f_title2.strip()[1:]

    # We should also zero pad the file, otherwise 1 and 10 will be grouped together.
    # To avoid that, we should pad it with zero in the front.

    f_no = f_no.strip()[1:].zfill(2)        # Padding is how wide you want it to be.

    # We can also do it 1 time in total.
    # f_title = f_title.strip()[1:]
    # f_no = f_no.strip()[1:].zfill(2)        # Padding is how wide you want it to be.
    # f_title2 = f_title2.strip()[1:]

    print('{}-{}-{}{}'.format(f_no, f_title,f_title2, file_ext))

    # This looks good. So, to rename a new file.
    new_name = '{}-{}{}'.format(f_no,f_title2, file_ext)

    os.rename(f, new_name)      # Rename original file to this new Name.