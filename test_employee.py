import unittest
from unittest.mock import patch
from employee import Employee
# We can use patch as a Decorator or as a CONTEXT MANAGER and it will allow us to mock an object during a test and then
# that object is Automatically restored after the test is run.

# We did mocking as we wont 1 Test to run independently of another test.
# If the site is down, we do not want that to effect our Test to fail.


class TestEmployee(unittest.TestCase):

    # We should have something which runs before anything.
    # and we should have something which runs after everything.
    # We have 2 Class methods. setUpClass and tearDownClass
    # class methods = Working with the class rather than the instance of the class.

    @classmethod
    def setUpClass(cls):
        print('setUpClass\n')
        # setupClass can be used to populate the database once before everything begins and
        # No need to populate database before every class.

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    # setUP will run before every single test.
    # tearDown will run after every single test.
    # Create those 2 functions.

    def setUp(self):
        print('setUP')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        # To access them from within our other tests, we have to set them as instance attributes, by putting self.emp_1 etc.
        # emp_1 = Employee('Corey', 'Schafer', 50000)
        # emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        print('test_email')
        # Add it in def setUp(self) instead.
        # emp_1 = Employee('Corey', 'Schafer', 50000)
        # emp_2 = Employee('Sue', 'Smith', 60000)
        # Since these are now Instance attributes, if you want to use them then make self.emp_1 and self.emp_2

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'        # changing the first names.
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')     # Email should change, when name changes
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        # Add it in def setUp(self) instead.
        # emp_1 = Employee('Corey', 'Schafer', 50000)
        # emp_2 = Employee('Sue', 'Smith', 60000)
        # Since these are now Instance attributes, if you want to use them then make self.emp_1 and self.emp_2

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_raise')
        # Add it in def setUp(self) instead.
        # emp_1 = Employee('Corey', 'Schafer', 50000)
        # emp_2 = Employee('Sue', 'Smith', 60000)
        # Since these are now Instance attributes, if you want to use them then make self.emp_1 and self.emp_2

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:      # We want to patch requests.get of employee module.
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')


            mocked_get.return_value.ok = False      # Check Bad Response
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

"""
# TEST DON'T NECESSARILY RUN IN ORDER.
setUpClass
setUP
test_raise
tearDown

setUP
test_email
tearDown

setUP
test_fullname
tearDown

tearDownClass

"""