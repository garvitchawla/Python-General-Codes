import requests

class Employee:
    '''A sample Employee Class.'''

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}, '{}', '{}')".format(self.first, self.last, self.pay)


    # Let's create another method below to be used for Mocking. Make sure we can get a URL
    # from a website, and return if the response is Okay otherwise say it's a Bad Response.
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')

        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
