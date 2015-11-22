#!/usr/bin/python3
while True:
    line = input('>>> ')
    print(line, 'is ' + ('' if line[::-1] == line else 'not ') + 'palindrome')
