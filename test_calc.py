
# The naming convention is when you write test in the beginning and then write what you want to do later.

import unittest
import calc

class TestCalc(unittest.TestCase):      # Inherit from unittest.TestCase
    # The method should start with test.
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)        # Assert Equal check that the result is 15.
        self.assertEqual(calc.add(5, 10), 15)       # Other way of writing above commands.
        self.assertEqual(calc.add(-1, 1), 0)  # Edge Cases.
        self.assertEqual(calc.add(-1, -1), -2)  # Edge Cases.
        # It checked the above assertEqual but it will still say that it 'Ran 1 test in 0.001s'.

        # self.assertEqual(result, 14)  # To check a case of Failure : 14.
        # Ran 1 test in 0.002s
        #
        # FAILED(failures=1)
        #
        # 14 != 15
        #
        # Expected: 15
        # Actual: 14

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)  # Edge Cases.
        self.assertEqual(calc.subtract(-1, -1), 0)  # Edge Cases.

    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 10), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)  # Edge Cases.
        self.assertEqual(calc.multiply(-1, -1), 1)  # Edge Cases.

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)  # Edge Cases.
        self.assertEqual(calc.divide(-1, -1), 1)  # Edge Cases.
        self.assertEqual(calc.divide(5, 2), 2.5)  # Edge Cases.

        self.assertRaises(ValueError, calc.divide, 10, 0)
        # First argument is the Exception that we expect, 2nd Argument is the function that we want to run.
        # 2nd argument is the function without passing arguments, so no paranthesis.
        # Arguments to be passed in the divide function separately.

        # self.assertRaises(ValueError, calc.divide, 10, 2)
        # AssertionError: ValueError not raised by divide

        # We can also use CONTEXT MANAGER using with
        with self.assertRaises(ValueError):
            calc.divide(10,0)


    """
    to RUN on TERMINAL:
    python - m unittest / Users / garvitchawla / PycharmProjects / NokiaInterview / test_calc.py
    python -m unittest testcalc.py    <==>     # Run on Terminal. Other way is to Running in main.
    """

    if __name__ == '__main__':                      # If you run this module directly, then run the code within the conditional.
        unittest.main()                             # code within is unittest.main()


    # The method name should be test_add only and not add_test.
    # The name should start with 'test'.

