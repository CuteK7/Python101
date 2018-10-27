# Python使用Unicode编码，支持多语言
print('我是一条包含中文的str')

# ord()字符转化编码，chr()编码转化字符
print(ord('A'), ord('中'), chr(66), chr(25991))

# 使用'\uxxxx'，xxxx十六进制表示Unicode字符
# 例如'中'，Unicode编码20013，十六进制0x4e2d，可以直接用chr(20013)表示，也可以直接用'\u4e2d'表示。
print('\u0041')

# 一般内存中会使用Unicode，str是字符串，传输、存储使用bytes
x = b'ABC'
print(b'ABC')

# 以Unicode表示的str通过encode()方法可以编码为置顶的bytes
# encode()方法可转化为utf-8、ascii，转化为bytes
# print('中'.encode('ascii'))
# UnicodeEncodeError: 'ascii' codec can't encode character '\u4e2d' in position 0: ordinal not in range(128)
print('中文'.encode('utf-8'))
print('ABC'.encode('utf-8'))

# b''为使用bytes使用decode()方法进行解码
# \xe4即utf-8下的0xe4，即11100100
# \xb8即utf-8下的0xb8，即10111000
# \xad即utf-8下的0xad，即10101101
# \u4e2d即unicode下的0x4e2d，0100111000101101
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad'.decode())

# 可以在decode()中传入errors='ignore'忽略解码错误
print(b'\xe6\x96\x87\x96\x87'.decode('utf-8', errors='ignore'))

# Bytes类型的字符按照\xe4为一个字符，一个中文字符Bytes为3
# str字符串按照实际字符进行计数
#
print(len(b'\xe4\xb8\xad'))
print(len(b'\xe4\xb8\xad'.decode('utf-8')))
print(len('中'))
print(len('中文'.encode('utf-8')))
print(len('ABC'.encode('ascii')), len('ABC'.encode('utf-8')))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 格式化
# %s替换字符串，%d替换整数，%f替换浮点数，%x替换十六进制数
# %s是万能替换符，%%表示转义%
print('Hi %s, your score is %d.' % ('Bart', 59))

# format()格式化，可以格式化{0},{1}替换
print('Hi {0}, your score is {1:.2f}.'.format('Bart', 59))

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85

r = (s2 - s1) / s1 * 100
print('%.1f%%' % r)

