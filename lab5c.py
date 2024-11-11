#!/usr/bin/env python3
# Author ID: jsingh1101

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if _name_ == '_main_':
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
