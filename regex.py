import re

emails = '''
garv1223-22@gmail.com
chawla.g@husky.neu.edu
'''

pattern = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+\.(com|edu|net)')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
