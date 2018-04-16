import sqlite3
from employee import Employee

# Connection object variable that represents our database.
# conn = sqlite3.connect(':memory:')        # That how you make a In-Memory Database.
# This gives a database that is in RAM, and that is useful for testing.

conn = sqlite3.connect('employee.db')
# Employee database. # This line will create 'employee.db' and connect to it.

# We cant open employee.db and see content.

# Now create a cursor which allows to execute sql commands. Cursor allows to create table and add data to it.

c = conn.cursor()

# Now, we can run using execute() method.

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

# If you run this again, it will say that table employees already exists. So, comment it out for future work


# Let's make 4 Functions to INSERT, SELECT, UPDATE and DELETE employees from a Database.
def insert_emp(emp):
    with conn:              # with connection.
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})         # Select statement doesnt need to be commited.
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay' : pay})
        # pay is the new one. Therefore, just 'pay'.


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


# After importing employee, we can create a couple of instances of this class.
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)


insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

'''
OLD WAY COMMENTED BELOW:

print(emp_1.first, emp_1.last, emp_1.pay)
print("{} {} earns {}".format(emp_1.first, emp_1.last, emp_1.pay))




c.execute("INSERT INTO employees VALUES ('Garvit', 'Chawla', 800000)")


c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))
# Above statement will work, but is a BAD practice as this is vulnerable to SQL Injection attacks.
# SQL Injection attack, we can set some values to the database, that particular value will break the entire database. AS its not properly ESCAPED.

# So, 2 better ways is
# 1. to have a ? in place of placeholder, and then have a tuple pass-in with all the values. No format way. = TUPLE way
# 2. To have a Dictionary, but first have a key then the value through the object. = DICTIONARY way

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
conn.commit()

# This way we have added values to the table employees.
# In the database we have ('Garv', 'Chawla', 50000), ('Garvit', 'Sexy', 800000)
# Comment them out after adding values to the database.

c.execute("SELECT * FROM employees WHERE last = 'Chawla'")
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last = ?", ('Chawla',))    # To make it into a Tuple, we have to give an extra ','. As there's only one Value.
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'Doe'}) # Even with 1 value, its more readable.
print(c.fetchall())


# print(c.fetchone())       # ('Garv', 'Chawla', 50000)
# print(c.fetchall())     # [('Garv', 'Chawla', 50000)]  This prints a List.
# It will get the next row in our results and only return that row. Returns 'None' if no more rows available.

# c.fetchmany(5)        # This will fetch 5 rows.
# fetchmany will return '5' that number of rows as a List.
# c.fetchall()          # This will get the remaining rows that our left and return those as a list and if no more rows then it returns Empty list.


# """ is a Dog string. Multiple lines."""

conn.commit()
# We're doing connection commit and NOT c. commit() NOT cursor commit() = ONLY Connection commit.
'''

conn.close()

