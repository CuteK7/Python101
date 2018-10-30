# -*- coding: utf-8 -*-
# Use for loop to print list items:
names = ['Bart', 'Lisa', 'Maggie']
for item in names:
    print(item)


# Use for loop to calculate the sum of integers from 1 to 100:
sum = 0
for x in range(1, 101):
    sum += x
print('The answer to 1+2+3+...+98+99+100={0}.\n'.format(sum))

# Function range():
# range(5) == [1, 5);
for x in range(5):
    print('Range(5) includes: %s.' % x)
L5 = list(range(5))
print(L5)


# While Loop:
sum = 0
n = 100
while n > 0:
    sum += n
    print('%s: %s' % (n, sum))
    n -= 1
print(sum)

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for item in L:
    print('Hello, %s!' % item)

# Use break to get out of loops:
n = 1
while n <= 100:
    if(n / 17 == 4):
        break
    print('%s is a safe number.' % n)
    n += 1
print('END')

# Use continue to skip a round.
# Case: Output all odd numbers in range(101):
n = 1
for n in range(101):
    if(n % 2 == 0):
        continue
    print('%s is an odd number in range(101).' % n)
print('END.')