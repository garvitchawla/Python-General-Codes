li = [9,1,8,2,5,6,7,3,4,10]

s_li = sorted(li)
print("**********LIST*********")

print("Sorted List\t\t\t\t", s_li)
print("Original List\t\t\t", li)

# Here the original is still unsorted.

# We can also sort the list. We can simply li.sort()

li.sort()
print("Original List\t\t\t", li)

# sorted() function provides a new sorted list and we provide it to a variable.
# sort() method sorts the list and returns none.
wrong_s_li = li.sort()
print(wrong_s_li)           # This returns None. sort() returns none. Use sorted() if you want to transfer it to some other variable.

# Now to see the List in DESCENDING ORDER. Use reverse = True
s_li = sorted(li, reverse=True)
print("Sorted List Reversed\t", s_li)

li.sort(reverse=True)
print("Original List Reversed\t", li)

# sort() works only on List. While, sorted() is more flexible, gives you more functions works on tuple.
print("*********TUPLE*********")

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# Tuple doesn't have a sort() method. But, it has sorted() function.

s_tup = sorted(tup)
print("Sorted Tuple\t\t\t", s_tup)

print("*******DICTIONARY******")

di = {'name':'Corey', 'job':'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print("Sorted Dictionary\t\t", s_di)

new_li = [-6, -5, -3, 1, 2, 3]
print("Original New List\t\t", new_li)
s_new_li = sorted(new_li)
print("Sorted New List\t\t\t", s_new_li)


# Let's sort them using the absolute value.
s_new_li = sorted(new_li, key=abs)      # Enter a key and allow absolute.
print("Absolute New List\t\t\t", s_new_li)



