# -*- coding: utf-8 -*-

# IF/ELSE: TREE WITH TRUE/FALSE BRANCHES
age = 20
if age >= 18:
    print('Your age is {0}'.format(age))
    print('You are an adult!')

age = 3
if age >= 18:
    print('Your age is {0}.'.format(age))
    print('You are an adult.')
elif age >= 10:
    print('Your age is {0}.'.format(age))
    print('You are a teenager.')
else:
    print('Your age is {0}.'.format(age))
    print('You are a child.')

# if x: pass
# When x is neither void, nor have the value of FALSE/0, then it's true.
x = ''
if x:
    print('There\'s a normal value stored in \'x\'.')
else:
    print('The value stored in \'x\' is abnormal.')


# INPUT: the value picked by input() method will be stored as a string.
# You need to force covert the string to a target type accordingly.

# yob = input('You birth in:\n')
# # if yob <2000:
# #     print('You are younger than 18 yrs old.\n')
# # else:
# #     print('You are elder than 18 yrs old.\n')
# #
# # Traceback (most recent call last):
# # File "C:/Users/Kevin-Office/IdeaProjects/Python101/04_basicPython/conditionJudgement.py", line 32, in <module>
# # if yob <2000:
# # TypeError: '<' not supported between instances of 'str' and 'int'

yob = input('You birth in:\n')
if int(yob) <2000:
    print('You are elder than 18 yrs old.\n')
else:
    print('You are younger than 18 yrs old.\n')


# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
#
# # -*- coding: utf-8 -*-
#
# height = 1.75
# weight = 80.5
# bmi = ???
# if ???:
#     pass

# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('Your BMI is {0}. You are too skinny.\n'.format(bmi))
elif bmi <= 25:
    print('Your BMI is {0}. Your weight is normal.\n'.format(bmi))
elif bmi <= 28:
    print('Your BMI is {0}. You are overweight.\n'.format(bmi))
elif bmi <= 32:
    print('Your BMI is {0}. You are fat.\n'.format(bmi))
elif bmi > 32:
    print('Your BMI is {0}. You are too fat.\n'.format(bmi))