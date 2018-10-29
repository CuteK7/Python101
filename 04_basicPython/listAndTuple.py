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


# Tuples are similar to lists. But the elements in tuples can not be changeable.
# Once a tuple is assigned, methods used in list such as append, insert can not be applied to tuples.
# Tuple elements can be called by the same way as you do to a list item.
classmatesTuple = ('Bart', 'Lisa', 'Maggie')
print('The first element in classmatesTuple is %s.' % classmatesTuple[0])
print('The last element in classmatesTuple is %s.\n' % classmatesTuple[-1])

# Because of the property of unchangeable, tuples are considered safer than lists.
# So they are widely used for safety reasons.
# Be aware that tuples containing singular element are defined in this way:
# IMPORTANT: YOU MUST USE A COMMA AFTER THE 'ONLY ELEMENT' SO THAT PYTHON CAN RECOGNIZE THE VALUE AS A TUPLE. OTHERWISE IT WILL BE RECOGNIZED AS AN ARITHMETIC EXPRESSION.
singularTuple = (1,)
fakeSingularTuple = (1)
print('The type of singularTuple is %s.\nBut the type of fakeSingularTuple is %s.\n' % (type(singularTuple), type(fakeSingularTuple)))


# 'Changeable' Tuple:
changeableTuple = ('a', 'b', ['A', 'B'])
changeableTuple[2][0] = 'X'
changeableTuple[2][1] = 'Y'

print('The changeable Tuple becomes {0}.\n'.format(changeableTuple))

# 练习
# 请用索引取出下面list的指定元素：
#
# # -*- coding: utf-8 -*-
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# # 打印Apple:
# print(?)
# # 打印Python:
# print(?)
# # 打印Lisa:
# print(?)



# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
