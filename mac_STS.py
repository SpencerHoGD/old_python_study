#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-09-09
hexiaoming
'''
import os

#file = '/Users/hexiaoming/Documents'


def wf():
    with open('./tmp/test-file.txt', 'w') as f:
        f.write('first line\nsecond line\nthird line\n')


def rf():
    with open('./tmp/test-file.txt', 'r') as f:
        for line in f.readlines():
            print(line)


def remove():
    f = './tmp/test-file.txt'
    if os.path.exists(f):
        os.remove(f)
        print(f'{f} had just been deleted.')
    else:
        print(f'{f} does not exists.')


if __name__ == '__main__':
    wf()
    rf()
    remove()
