# -*- coding: utf-8 -*-


# dict: abbr. of dictionary, a.k.a. map in other languages, uses key-value
# structure to store information. Pro: fast to lookup values. {}
# Use dictName['key'] to get values.
d = {'Bart': 59, 'Lisa': 100, 'Maggie': 95}
print(d['Bart'])

# Change value by specific key:
d['Maggie'] = 96
print(d)

# print(d['Homer'])
# Will cause error 'cuz key 'Homer' is not exist.
# File "C:/Users/Kevin-Office/IdeaProjects/Python101/04_basicPython/dictAndSet.py", line 14, in <module>
# print(d['Homer'])
# KeyError: 'Homer'

# Check if the specific key is in the dictionary:
print('Is Homer in the list? %s' % ('Homer' in d))
