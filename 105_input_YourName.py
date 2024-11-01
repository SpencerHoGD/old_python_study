#! /usr/bin/env python3

# 初始化name为空，用while循环一直到“接受的输入正确”为止。打印感谢。
name = ''
while name != 'your name':
    print('please enter your name.')
    name = input()
print('Thank you! ')
