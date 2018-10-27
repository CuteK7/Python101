# -*- coding: utf-8 -*-

# list ['','',''] 有序
classmates = ['Kevin', 'Jason', 'Barney']
print(classmates)
print('The length of classmates list is %d' % len(classmates))

# List Index from 0 to len(classmates) - 1
# The last index is -1
print(classmates[0], classmates[1], classmates[2])
print('The last classmate is %s.' % classmates[-1])

# Lists are changeable. You can append, insert, pop.
# Append means add a new list item at the end of a list.
classmates.append('Ted')
print('Ted is appended to the last in %s.\n' % classmates)

# Insert means insert a new list item at an appointed position.
classmates.insert(2, 'Marshall')
print('Marshall is added to 2nd place in %s.\n' % classmates)

# Pop can delete an appointed list item, or the last item by default.
classmates.pop(1)
print('Classmate[1] has been removed from the list: %s.\n' % classmates)

# Reassign values to list item
classmates[1] = 'Lily'
print('Classmate[1] has been replaced to Lily in the list: %s\n' % classmates)

# List items can be any type. Even a list can be stored as a single list item.
L = ['Python', ['C', 'C++'], 3.141592653589]
print('Although L contains a list as item[1], L\'s length is %d\n' % len(L))

# Void List
voidList = []
print('The length of voidList is %d.\n' % len(voidList))
