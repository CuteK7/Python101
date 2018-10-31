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

# Two ways to check if the specific key is in the dictionary:
print('Is Homer in the list? %s' % ('Homer' in d))

print(d.get('Homer'))

print(d.get('Homer', -9999))


# Delete dict items by using pop() method.
d.pop('Maggie')
print(d)

# Notes:
# The sequences of dict items have NOTHING to do with the chronological order that they are stored in the dict.
# Comparing to List, Dict has such features as follows:
# Higher IO than List, regardless of the size of a dict;
# Larger RAM consumption.
# Keys in dict are unchangeable!!!
# So unchangeable elements including strings, integers can be used as keys, while changeable elements such as lists CANNOT be used as keys.


# Set {1, 2, 3}
# Create a set:
# s = set([1, 2, 3])
s = {1, 2, 3}
print('The type of s is %s. It\'s value is %s.' % (type(s), s))

# No element will be stored more than once in a single set.
# Elements are unordered in a set.
# s = set([1, 1, 2, 3, 3])
s = {1, 1, 2, 3, 3}
print('The value of s is %s. The length of s is %s' % (s, len(s)))

# Use add() method and remove() method to edit a set.
s.add(4)
print(s)

s.remove(2)
print(s)

# Usage of set:
# For mathematical purposes: and/or expressions
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# And calculation:
print('The answer to s1 & s2 is %s' % (s1 & s2))

# Or calculation:
print('The answer to s1 | s2 is %s' % (s1 | s2))

# tSet = set([1, (2, 3, 4)])
tSet = {1, (2, 3, 4)}

print(tSet)
