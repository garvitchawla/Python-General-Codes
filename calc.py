
def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Subtract Function"""
    return x * y

def divide(x, y):
    """Subtract Function"""
    if(y == 0):
        raise ValueError('Can not divide by 0!')
    return x / y


# print(add(10, 5))       # 15
# The naming convention is when you write test in the beginning and then write what you want to do later. test_calc.py


