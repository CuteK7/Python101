# -*- coding: utf-8 -*-
# Built-in Function Documentation: https://docs.python.org/3/library/functions.html

x = -100
print('x = %s, abs(x) = %s.' % (x, abs(x)))

L = [1, 2, 3, 5]
t = (1, 2, 3, 7)
s = {1, 2, 3, 6}
print('The max item in list L is %s.' % max(L))

# Type conversion:
print('The type is %s. The value is %s.' % (type(int('123')), int('123')))
print('The type is %s. The value is %s.' % (type(int(12.34)), int(12.34)))
print('The type is %s. The value is %s.' % (type(str(1.23)), str(1.23)))
print('The type is %s. The value is %s.' % (type(str(100)), str(100)))
print('The type is %s. The value is %s.' % (type(bool(1)), bool(1)))
print('The type is %s. The value is %s.' % (type(bool('')), bool('')))

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
#
# # -*- coding: utf-8 -*-
#
# n1 = 255
# n2 = 1000

# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000
print('The two numbers are %s and %s.' % (hex(n1), hex(n2)))