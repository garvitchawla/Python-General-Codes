
# f = open(testfile.txt)      # our file name is test_file.txt
#
# try:
#     pass
#
# except Exception:
#     pass

try:
    f = open('test_file.txt')       # Incorrect file names throws FileNotFoundException.
    g = open('corrupt.txt')         # Using this file to manually raise an Exception.
    if g.name == 'corrupt.txt':
        raise Exception             # Raising Exception manually.
    # var = bad_var
except FileNotFoundError: 
    print("File not found Error.")
# except NameError:
#     print("It's a name Error.")
except NameError as e:
    print(e)                            # name 'bad_var' is not defined
except Exception:
    print("General Exception")          # More general exception at the bottom.

else:                                   # Else runs when there is no Exception caught. 'Try' runs smoothly.
    print(f.read())                     # Prints some random test file.
    f.close()

    print(g.read())
    g.close()
finally:                                # Finally always executes, whether there's an Exception or not.
    print("Executing the Finally...")


