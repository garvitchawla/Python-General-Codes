
'''
PROGRAM 1:

print("Hello World!")
'''


'''
PROGRAM 2:
Add 2 numbers.

num1 = 3.6
num2 = 2.4

sum = num1 + num2

print(sum)

'''


'''
PROGRAM 3:
Python program to find the square root.

num = 2.4
num_sqrt = 2.4 ** 0.5
print("Square root of %0.3f is %0.3f" %(num, num_sqrt))

OR

# Take Input from User.
num = float(input("Enter a number! \n"))
num_sqrt = num ** 0.5
print("Square Root of %0.3f is %0.3f" %(num, num_sqrt))

OR

# For complex numbers
import cmath
#num = 1 + 2j
# Enter a Complex number, a + bj

num = eval(input("Enter a Complex Number!\n"))
num_sqrt = cmath.sqrt(num)
print("The square root of {0} is {1:0.3f} + {2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))
'''


'''
PROGRAM 4:
Calculate Area of a Triangle


a = float(input("Enter 1st Side\n"))
b = float(input("Enter 2nd Side\n"))
c = float(input("Enter 3rd Side\n"))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of a triangle with sides %0.2f, %0.2f, %0.2f is %0.2f" %(a, b, c, area))
'''


'''
PROGRAM 5:
Python Program to Solve Quadratic Equation
# Solve the quadratic equation ax**2 + bx + c = 0


import cmath
a = float(input("Enter a:\n"))
b = float(input("Enter b:\n"))
c = float(input("Enter c:\n"))

d = (b**2) - (4*a*c)

sol2 = (-b - cmath.sqrt(d))/(2*a)
sol1 = (-b + cmath.sqrt(d))/(2*a)

print("The Solution is {} and {}".format(sol1, sol2))
'''

'''
PROGRAM 6:
Swap to Variables


x = input("Enter 1st no.")
y = input("Enter 2nd no.")

temp = x
x = y
y = temp

print("The value of x after swapping is {}".format(x))
print("The value of y after swapping is {}".format(y))

'''

'''
PROGRAM 7:
Generate a RANDOM Number

import random

rand_num1 = random.randrange(0,100)
rand_num2 = random.randint(0,9)

print("The two random numbers are {} and {}".format(rand_num1, rand_num2))
'''

'''
PROGRAM 8:
Convert Kilometers to Miles


kilometers = float(input("Enter distance in kilometers.\n"))
con_value = 0.621371

miles = con_value * kilometers
print("Miles are %0.3f" %miles)
'''

'''
PROGRAM 9:
Convert temperature in celsius to fahrenheit

celsius = float(input("Enter Temperature in Celsius!\n"))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
'''

'''
PROGRAM 10:
Using IF, ELIF, ELSE


num = float(input("Enter a number to check if its _ve, -ve or 0\n"))
if num > 0:
    print("Positive Number")
elif num == 0:
    print("It's 0")
else:
    print("It's a negative number!")
'''

'''
PROGRAM 11:
Number is odd or even

num = int(input("Enter a number!\n"))
if num % 2 == 0:
    print("{0} {1} is Even.".format(num, num))
else:
    print("{0} is Odd.".format(num))
'''


'''
PROGRAM 12:
Program to Check Leap Year
A leap year is exactly divisible by 4 except for century years (years ending with 00). 
The century year is a leap year only if it is perfectly divisible by 400. For example,

2017 is not a leap year
1900 is a not leap year
2012 is a leap year
2000 is a leap year


year = int(input("Enter a year!\n"))

if((year % 4) == 0):
    if((year % 100) == 0):
        if((year % 400) == 0):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is NOT a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is a leap year".format(year))

'''


'''
PROGRAM 13:
Largest among 3 numbers!

num1 = float(input("Enter the 1st Number!\n"))
num2 = float(input("Enter the 2nd Number!\n"))
num3 = float(input("Enter the 3rd Number!\n"))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number between", num1, ",", num2, "and", num3, "is", largest)

'''

'''
PROGRAM 14:
Check if Prime Number.


num = int(input("Enter a number!\n"))

if num > 1:
    for i in range(2, num):
        if ((num % i) == 0):
            print(num, "is not a prime number.")
            print(i, "times", num//i, "is", num)
            break

    else:
        print(num, "is a prime number.")

else:
    print(num, "is not a Prime number.")

'''


'''
PROGRAM 15:
Prime Numbers in an Interval

lower = int(input("Enter lower bound number.\n"))
upper = int(input("Enter upper bound number.\n"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                break

        else:
            print(num, " ", end="")
'''


'''
PROGRAM 16:
Factorial of a Number


num = int(input("Enter a number!\n"))

if num < 0:
    print("Factorial only for Positive Numbers!")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num):
        num = num * i

print("Number is %d" %num)
'''


'''
PROGRAM 17:
Multiplication Table

num = int(input(("Enter a number!\n")))

for i in range(1, 11):
    print(num, "x", i, "is", num * i)
'''


'''
PROGRAM 18:
Fibonacci Series

nterms = int(input("Enter number of fibonacci terms you want?\n"))

n1 = 0
n2 = 1
count = 0

if(nterms < 0):
    print("Enter +ve number!")

elif nterms == 1:
    print("Fibonacci series upto", nterms, ":", n1)

else:
    print("Fibonacci series upto n terms")
    while count < nterms:
        if(count < nterms - 1):
            print(n1, end=",")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count = count + 1

        else:
            print(n1)       # to remove last ,
            break
'''


'''
PROGRAM 19:
Armstrong Number


num = int(input("Enter Number.\n"))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10   # make it an integer value.

if num == sum:
    print("%d is an Armstrong number" %num)
else:
    print("%d is NOT an Armstrong number" %num)
'''

'''
PROGRAM 20:
check Armstrong numbers in certain interval


lower = int(input("Enter lower bound!\n"))
upper = int(input("Enter upper bound!\n"))

for num in range(lower, upper + 1):
    sum = 0

    order = len(str(num))

    temp = num

    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** order)            // 1634 = (1 ^ 4) + (6 ^ 4) + (3 ^ 4) + (4 ^ 4)
        temp = temp // 10

    if num == sum:
        print(num)

'''

'''
PROGRAM 21:
Sum of Natural Numbers


num = int(input("Tell me a POSITIVE number of Numbers you want to add!\n"))

if num < 0:
    print("Enter a POSITIVE number")

else:
    sum = 0
    while(num>0):
        sum = sum + num
        num = num-1
    print("The Sum is %d" %sum)

'''


'''
PROGRAM 22:
display the powers of 2 using anonymous function

terms = int(input("How many terms? "))


# def function1(x):
#    return 2 ** x

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print(result)
# display the result

print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
'''


'''
PROGRAM 23:
Find Numbers Divisible by Another Number


num_div = int(input("Enter a Number to divide by\n"))
any_list = [int(x) for x in input().split()]

# OR

my_list = [12, 65, 54, 39, 102, 120]

empty_list = []

print(any_list)
print(my_list)


def div():
    for i in any_list:
        if(i % num_div == 0):
            empty_list.append(i)

    print(empty_list)

div()

'''


'''
PROGRAM 24:
# Python program to convert decimal number into binary, octal and hexadecimal number system

# Change this line for a different result
dec = int(input("Enter a Decimal Number"))

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")

'''

'''
PROGRAM 25:
print ASCII value
c = input("Enter a character: ")

print("The ASCII value of '" + c + "' is",ord(c))

'''


'''
PROGRAM 26:
HCF of 2 input numbers:


def computeHCF(x,y):
    if x > y:
        smallest = y
    else:
        smallest = x
    for i in range(1, smallest + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

num1 = int(input("Enter first number!\n"))
num2 = int(input("Enter second number!\n"))

print("HCF of %d and %d is %d" %(num1, num2, computeHCF(num1, num2)))
'''


'''
PROGRAM 27:
LCM of 2 numbers


def computeLCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater = greater + 1

    return lcm

# LCM for 3 & 9 is 9 and for 3 & 8 is 24.

num1 = int(input("Enter the first number!\n"))
num2 = int(input("Enter the second number!\n"))

print("The LCM of %d and %d is %d" %(num1, num2, computeLCM(num1, num2)))
'''


'''
PROGRAM 28:
Factors of a Number


alist = []

# range(5) goes from 0 to 4, but total is 5.
# range(2, 5) goes from 2, 3, 4, But not 5.

def factors(x):
    for i in range(1, x + 1):
        if(x % i == 0):
            alist.append(i)
            print(i, end=" ")

    print("\n", alist)


num = int(input("Enter a number!\n"))
factors(num)

'''


'''
PROGRAM 29:
Simple Calculator


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation!\n")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
choice = int(input("Enter your choice:\n"))


if choice == 1:
    print("Sum of %d and %d is %d" %(num1, num2, add(num1, num2)))
elif choice == 2:
    print("Difference of %d and %d is %d" %(num1, num2, subtract(num1, num2)))
elif choice == 3:
    print("Multiplication of %d and %d is %d" %(num1, num2, multiply(num1, num2)))
elif choice == 4:
    print("Division of %d and %d is %d" %(num1, num2, divide(num1, num2)))

else:
    print("Wrong Input!")
'''


'''
# Calculator with many Inputs

def add(x,y):
    ans = x + y
    return ans

def subtract(x,y):
    ans = x - y
    return ans

def multiply(x, y):
    ans = x * y
    return ans

def divide(x, y):
    ans = x / y
    return ans

def operation():

    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))

    print("Select Operation!")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = int(input("Enter your choice:\n"))

    if choice == 1:
        print("Sum of %d and %d is %d" % (num1, num2, add(num1, num2)))
    elif choice == 2:
        print("Difference of %d and %d is %d" % (num1, num2, subtract(num1, num2)))
    elif choice == 3:
        print("Multiplication of %d and %d is %d" % (num1, num2, multiply(num1, num2)))
    elif choice == 4:
        print("Division of %d and %d is %d" % (num1, num2, divide(num1, num2)))
    else:
        print("Wrong Input!")

operation()

def controller():
    yes_no = "yes"
    while(yes_no):
        print("Do you want to continue?\n")
        if(input() == "yes"):
            # new_num = int(input("Enter a new number.\n")
            operation()

        else:
            exit()


controller()
'''


'''
PROGRAM 30:
Reverse a String.

# Way 1 - Using Loops
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("Enter a String.\n")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))


# Way 2 - Using Recursion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

# In the function, the base condition is that if the length of the string is equal to 0, the string is returned.
# If not equal to 0, the reverse function is recursively called to slice the part of the string except the first character
# and concatenate the first character to the end of the sliced string.

s = input("Enter a String.\n")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))


# Way 3 - Extended Slice
def reverse(string):
    string = string[::-1]               # start, stop and step. -1 denotes start from back and end at beginning
    return string

s = input("Enter a String.\n")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))

# Way 4 - Using Reversed
def reverse(string):
    string = "".join(reversed(string))
    return string


s = input("Enter a String.\n")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using reversed) is : ", end="")
print(reverse(s))

Way 1 - Using Loops AGAIN
def reverse(s):
    try:
        rev_str = ""

        for i in s:
            rev_str = i + rev_str
        return rev_str

    except ValueError:
        print("Wrong input")


s = input("Enter a String.\n")
print("Reverse is %s" %reverse(s))

'''


'''
PROGRAM 31
Palindrome


def reverse(s):
    str = ""

    for i in s:
        str = i + str

    return str

s = input("Enter a String!\n")
if s == reverse(s):
    print("Palindrome")
else:
    print("Not Palindrome")
'''


'''
PROGRAM 32:
Remove Punctuations From a String


punctuations = "!@#$%^&*()_+"

s = input("Enter a String")
print(s)

no_punc = ""

for char in s:
    if char not in punctuations:
        no_punc  = no_punc + char

print(no_punc)
'''


'''
PROGRAM 33:
Sort Words in Alphabetical Order


my_str = input("Enter a String\n")
words = my_str.split()
words.sort()
print("The Sorted words are:", end=" ")
for word in words:
    print(word, end=" ")
'''


'''
PROGRAM 34:
Illustrate Different Set operations


E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)

# set symmetric difference
print("Symmetric difference of E and N is", (E | N) - (E & N))

'''


'''
# PROGRAM 35:
# Count the number of each Vowel


# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# change this value for a different result
ip_str = 'Hello, have you tried our tutorial section yet?'

# uncomment to take input from the user
#ip_str = input("Enter a string: ")

# make it suitable for case-less comparisons
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)       # count is a dictionary.
# dictionary method fromkeys() to construct a new dictionary with each vowel as its key and all values equal to 0. 

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
# {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

'''


'''
PROGRAM 36:
REGEX = Regular Expressions

a, X, 9
ordinary characters just match themselves exactly.

. ^ $ * + ? { [ ]  | ( ) 
meta-characters with special meanings (see below)
 
. (a period)
matches any single character except newline 'n'

w    
matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. 
It only matches a single character not a whole word.

W 
matches any non-word character.

w+
matches one or more words / characters

b 
boundary between word and non-word

s 
matches a single whitespace character, space, newline, return, tab, form

S 
matches any non-whitespace character.

t, n, r 
tab, newline, return

D
matches anything but a digit

d 
matches a decimal digit [0-9]

d{1,5}
matches a digit between 1 and 5 in lengths. 

{n} d{5}
matches for 5 digits in a row

^
match the start of the string

$
match the end of the string end

*
matches 0 or more repetitions

?
matches 0 or 1 characters of whatever precedes it

use . to match a period or  to match a slash. 

If you are unsure if a character has special meaning, such as '@', you can
put a slash in front of it, @, to make sure it is treated just as a character.


The findall() is probably the single most powerful function in the re module
and we will use that function in this script. 

In the example below we create a string that have a text with many email
addresses.

We then create a variable (emails) that will contain a list of all the found
email strings. 

Lastly, we use a for loop that we can do something with for each email string
that is found. 



import re

str = "hello yellow some@gmail.com, blah blah some2@gmail.com"

# Here re.findall() returns a list of all the found email strings

emails = re.findall(r'[w.-]+@[w.-]+',str)

for email in emails:
    print(email)

We can also apply this for files. If you have a file and want to iterate over
the lines of the file, just feed it into findall() and let it return a list of
all the matches in a single step

read() returns the whole text of a file in a single string.


f = open("test.txt", 'r')
strings = re.findall(r'some pattern', f.read())


The re.search() method takes a regular expression pattern and a string and
searches for that pattern within the string.

The syntax is re.search(pattern, string).

where:
pattern = regular expression to be matched.

string = the string which would be searched to match the pattern anywhere in the string.

This example searches for the pattern 'word:' followed by a 3 letter word.

The code match = re.search(pat, str) stores the search result in a variable
named "match".

Then the if-statement tests the match, if true the search succeeded and
match.group() is the matching text (e.g. 'word:cat').

If the match is false, the search did not succeed, and there is no matching text.


import re
str = 'an example word:cat!!'
match = re.search(r'word:www',str)
if match:
    print("found",match.group())

else:
    print("couldnt find")


import re

programming = ["Python", "Perl", "PHP", "C++", "Basic", "somethingi", "somethingH"]

pat = "^B|^P|i$|H$"

for lang in programming:

    if re.search(pat, lang, re.IGNORECASE):
        print(lang, "FOUND")

    else:
        print(lang, "NOT FOUND")


# The re.sub() function in the re module can be used to replace substrings. 
# 
# The syntax for re.sub() is re.sub(pattern,repl,string). 
# 
# That will replace the matches in string with repl. 
# 
# In this example, I will replace all occurrences of the re pattern ("cool") 
# in string (text) with repl ("good").
    

import re
text = "Python is a cool language"
pattern = re.sub("cool","good",text)
print(pattern)


# Let's see two examples, using the re.compile() function.
# 
# The first example checks if the input from the user contains only letters,
# spaces or . (no digits)
# 
# Any other character is not allowed.


import re
name_check = re.compile(r"[^A-Za-zs.]")
name = input("Please, enter your name: ")

while name_check.search(name):
    print("Please enter your name correctly!")
    name = input("Please, enter your name: ")

print(name)


import re
phone_check = re.compile(r"[^0-9s-()]")
phone = input("Enter number")
while phone_check.search(phone):
    print("Enter number correctly")
    phone = input("Enter number")


Find Email Domain in Address
@
scan till you see this character

[w.]
a set of characters to potentially match, so w is all alphanumeric characters,
and the trailing period . adds to that set of characters.

+
one or more of the previous set.

Because this regex is matching the period character and every alphanumeric
after an @, it'll match email domains even in the middle of sentences.


import re
s = "My name is Garv and my email id is chawla.g@husky.neu.edu."

domain = re.search("@[w.]+",s)
print(domain.group())

# CLASSES
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())

# prints the following:
#
# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!


# Notice the following: all animals "talk", but they talk differently.
# The "talk" behavior is thus polymorphic in the sense that it is realized differently depending on the animal.
# So, the abstract "animal" concept does not actually "talk",
# but specific animals (like dogs and cats) have a concrete implementation of the action "talk".


# INHERITANCE
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()      # Object created.
t.inputSides()
t.dispSides()
t.findArea()

# Enter side 1 : 3
# Enter side 2 : 4
# Enter side 3 : 5
# Side 1 is 3.0
# Side 2 is 4.0
# Side 3 is 5.0
# The area of the triangle is 6.00
'''