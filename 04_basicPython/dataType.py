print('''hello,\n
world''')

print(True)
print(type(True))
print(3 > 5)

print(not 1 > 2)

age=input('Please input your age:\n')
if int(age) >= 18:
    print('adult')
else:
    print('teenager')

a = 'ABC'
b = a
a ='XYZ'
print(b)

PI = 31415926e-7

print(10/3)

print('Exercise:')
print('***************')
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n, '\n', f, '\n', s1, '\n', s2, '\n', s3, '\n', s4)