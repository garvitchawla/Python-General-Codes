import random
import sys
import os

print("Hello")  # To print "Hello".

# comment

'''
mutiline comments
'''

name = "Garv"

print(name)

# Numbers, Strings, Lists, Tuples, Dictionaries or Map

name = 15   # No need to write Int.

# + - / * // (this will divide and then make the remainder to nearest integer, if after division you get 14.5 it will become 14) ** (raise to power)

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 // 2 = ", 5//2)
print("5 ** 2 = ", 5**2)
print("5 % 2 = ", 5%2)

quote = "\"Always remember you are unique"
print(quote)                              # "Always remember you are unique

multi_line_quote = '''
JUST 
    like everyone else'''

'''
"Always remember you are unique 
JUST 
    like everyone else
'''
print("\n")
print("%s %s" %(quote, multi_line_quote))
print("\n")
print("%s %s %s" %("I love the quote",quote,multi_line_quote))


# LISTS   # Lists are in brackets.
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']

print(grocery_list[0])   # print specific item, 0.
print("First Item:", grocery_list[0])     # First Item: Juice

grocery_list[0] = "Green Juice"           # First Item: Green Juice
print("First Item:", grocery_list[0])

print(grocery_list[1:3]) # not including 3       # ['Tomatoes', 'Potatoes']
# OR
list1 = grocery_list[1:3]  # creating a new List.
print(list1)                # ['Tomatoes', 'Potatoes']

# new list.
other_events = ['wash car', 'pick up kids',
                'have fun']

# Create a 2D List. This will be a List of lists.
to_do_list = [other_events, grocery_list]   # made of 2 Lists.
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas']]

print((to_do_list[1][1]))   # Tomatoes  # First '1' is for List 2 (index 1) and then '1' means 2nd item in that 2nd list (index 1).

grocery_list.append('Onions')
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']]

grocery_list.insert(1, "Pickle")
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Green Juice', 'Pickle', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']]

grocery_list.remove('Pickle')
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']]

grocery_list.sort()
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Bananas', 'Green Juice', 'Onions', 'Potatoes', 'Tomatoes']]

grocery_list.reverse()
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Tomatoes', 'Potatoes', 'Onions', 'Green Juice', 'Bananas']]

del grocery_list[4]
print(to_do_list)           # [['wash car', 'pick up kids', 'have fun'], ['Tomatoes', 'Potatoes', 'Onions', 'Green Juice']]

to_do_list2 = other_events + grocery_list   # This will concatenate the List.

print(to_do_list2)          # ['wash car', 'pick up kids', 'have fun', 'Tomatoes', 'Potatoes', 'Onions', 'Green Juice']

to_do_list3 = [other_events, grocery_list]
print(to_do_list3)          # [['wash car', 'pick up kids', 'have fun'], ['Tomatoes', 'Potatoes', 'Onions', 'Green Juice']]  # This will again create a 2D List.

print(len(to_do_list2))     # 7
print(max(to_do_list2))     # wash car
print(min(to_do_list2))     # Green Juice


# TUPLE
# The difference between a tuple and Lists is that you cannot change TUPLE after assigning, but we can modify or change Lists according to need.
# LISTS = MUTABLE.  Lists are shown in Square Brackets.
# TUPLE = IMMUTABLE. Tuple are shown in Round Brackets.
pi_tuple = (3,1,4,1,5,9)
print(pi_tuple)             # (3, 1, 4, 1, 5, 9)

new_tuple_list = list(pi_tuple) # converting a TUPLE (Immutable objects) to a LIST (Mutable objects).
print(new_tuple_list)       # [3, 1, 4, 1, 5, 9]


# Dictionaries: A unique key for every value. It's in Curly Brackets.
# Values of a Dictionary are Mutable.
super_villains = {'Fiddler':"Isaac",
                  'Captain gold':'leonard',
                  'pied pipper':'thomas'}

print(super_villains['Captain gold'])   # leonard
del super_villains['Fiddler']
super_villains['pied pipper'] = 'Hartley'  # Changed Thomas -> Hartley.
print(len(super_villains))      # 2

print(super_villains.get("pied pipper"))    # Hartley

print(super_villains.keys())        # dict_keys(['Captain gold', 'pied pipper'])

print(super_villains.values())      # dict_values(['leonard', 'Hartley'])


# CONDITIONALS
# if, else, elif
age = 30
if age>16:
    print("you are old enough to drive")   # you are old enough to drive
else:
    print("You are not")

if age>=21:
    print("You are old enough to drive a tractor trailer")      # You are old enough to drive a tractor trailer.

# LOGICAL and or not
if ((age>1) and (age<=18)):
    print("You get a birthday")
elif not(age==30):
    print("You dont get a birthday party.")
else:
    print("You get a birthday party, Yeah!")                # You get a birthday party, Yeah!


# LOOPING
# Perform an action a set number of times.
for x in range(0,10):
    #print(x, '')
    print(x, "" , end="")   # 0 1 2 3 4 5 6 7 8 9 0
    # When we type like this, it wont take you to the next line after printing the first print command. So, All printed in 1 single line.

for y in range(0,10):
    print(y)

'''
1
2
3
4
5
6
7
8
9
'''

print("")

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
for z in grocery_list:
    print(z)

'''
Juice
Tomatoes
Potatoes
Bananas
'''

for x in [2,4,6,8,10]:
    print(x)

'''
2
4
6
8
10
'''

print()
num_list = [[1,2,3], [10,20,30], [100,200,300]]


for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

'''
1
2
3
10
20
30
100
200
300
'''
# Using While loop, when there is no idea how to do.

random_num = random.randrange(0,100) # Works from 0 to 99.
print()

while(random_num != 15):
    print(random_num)  # print if not 15.
    random_num = random.randrange(0,100) # change random number

# This will print any number between 0, 99 unless you get 15.

i = 0;

while(i<=20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i +=1          #   OR    i = i+1 This else is when the 'i' is odd.
        continue       # continue will leave all the code after this statement which is inside the while loop and will jump directly to while loop at the top.

    i += 1             # This will increase i by 1, for all even numbers.

print()

# Functions
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum       # sumNum is out of scope outside function

print(addNumber(1,4))   # 5

'''
print("Whats your name?")
name = sys.stdin.readline()
print("Hello", name)
'''

long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4])         # I'll

print(long_string[-5:]) # to show last 5 characters  # Floor

print(long_string[:-5]) # to show everything UPTO last 5 characters      # I'll catch you if you fall - The

print(long_string[0:-5]) # to show everything UPTO last 5 characters     # I'll catch you if you fall - The

print(long_string[:4]+" be there")      # I'll be there

print("%c is my %s letter and my number %d number is %.5f"
      %('X', 'favorite', 1, .14))       # X is my favorite letter and my number 1 number is 0.14000

print(long_string.capitalize())         # I'll catch you if you fall - the floor

print(long_string.find("Floor"))        # 33

print(len(long_string))                 # 38

print(long_string.replace("Floor", "Ground"))   # I'll catch you if you fall - The Ground

print(long_string.strip())  # this is to strip any white spaces in the string. There is none in this case.
                                        # I'll catch you if you fall - The Floor

quote_list = long_string.split(" ")     # To make a List
print(quote_list)                       # ["I'll", 'catch', 'you', 'if', 'you', 'fall', '-', 'The', 'Floor']


# FILE i/o ie File Input/output
test_file = open("test.txt", "wb")      # wb for output on screen
print(test_file.mode)                   # wb
print(test_file.name)                   # test.txt
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

# Open again as already closed and read the file
test_file = open("test.txt", "r+") # for reading and writing
text_in_file = test_file.read()    # Read the file
print(text_in_file)                # Write me to the file

# Delete the file
os.remove("test.txt")



# OBJECTS
class Animal:
    __name = ""  # Or __name = None which is a lack of a value.
    __height = 0  # by preceding with 2 underscores, these are going to be the private.
    # We have to make a function inside the class to change them and to get those value we need a function
    __weight = 0
    __sound = 0


    def __init__(self, name, height, weight, sound):  # self automatically, which it allows object to refer to itself.
        # no Animals exists, self provides a way.
        # self is like 'this' in java.
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    def set_name(self, name): # No animals exists, to add self provides. I m gonna change the object 'self'
        self.__name = name      # verifying that the data is good.

    def get_name(self):
        return self.__name    #


    def set_height(self, height): # No animals exists, to add self provides. I m gonna change the object 'self'
        self.__height = height

    def get_height(self):
        return self.__height


    def set_weight(self, weight): # No animals exists, to add self provides. I m gonna change the object 'self'
        self.__weight = weight

    def get_weight(self):
        return self.__weight


    def set_sound(self, sound): # No animals exists, to add self provides. I m gonna change the object 'self'
        self.__sound = sound

    def get_sound(self):
        return self.__sound


    def get_type(self):
        print("Animal")     # print ClassName

    def toString(self):     # Another way to write is using {}.
        return "{} is {}cm tall and {} kilograms and say {}.". format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound
                                                                     )


cat = Animal("Whiskers", 33, 10, 'Meow')
print(cat.toString())                   # Whiskers is 33cm tall and 10 kilograms and say Meow.



# INHERITANCE
# Inherit from other class, you get variables, functions etc
class Dog(Animal):   # Dog inheriting from Animal class
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):  # We can overwrite for constructor  # Added owner.
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)  # Calling super class of Dog ie Animal.

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):  # overwrite function
        return "{} is {}cm tall and {} kilograms and say {}. His owner is {}". format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)



# METHOD OVERLOADING
# able to perform based on attributes that is send in.
    def multiple_sounds(self, how_many=None): # that is how many is not important
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Garv") # Dog object
print(spot.toString())


# POLYMORPHISM
# Do different tasks based on the attributes that are sent in.
# Allows to refer to objects as there superclass and then
# automatically have the correct function called automatically.

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat) # cat is Animal object  # Animal
test_animals.get_type(spot) # Dog

spot.multiple_sounds(4)         # RuffRuffRuffRuff
spot.multiple_sounds()