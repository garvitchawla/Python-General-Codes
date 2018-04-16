# Sort Employee Class

class Employee():
    def __init__(self, name, age , salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)
        # This is how it will be actually represented when displayed on the screen.


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]     # added employees into a List.

def e_sort(emp):
    return emp.name

# s_emplyees = sorted(employees)
# print(s_emplyees)
# TypeError: '<' not supported between instances of 'Employee' and 'Employee'
# We have to give a key.

s_emplyees = sorted(employees, key=e_sort)
print(s_emplyees)
# Sorts it in bases of Name.
# [(Carl, 37, $70000), (John, 43, $90000), (Sarah, 29, $80000)]

s_emplyees = sorted(employees, key=e_sort, reverse=True)
print(s_emplyees)
# Sorts it in Descending Order. [(Sarah, 29, $80000), (John, 43, $90000), (Carl, 37, $70000)]

# If we don't want the e_sort method we can use Lambda function.
s_emplyees = sorted(employees, key = lambda e: e.name)
print(s_emplyees)
# This time using Lambda function. [(Carl, 37, $70000), (John, 43, $90000), (Sarah, 29, $80000)]



# We can do 1 MORE WAY, without using LAMBDA functions and without using a different e_sort() method.
# Use ATTRGETTER
# from operator import attrgetter
from operator import attrgetter
s_emplyees = sorted(employees, key=attrgetter('age'))       # On basis of Age.
print(s_emplyees)
# Using attrgetter -> [(Sarah, 29, $80000), (Carl, 37, $70000), (John, 43, $90000)]
