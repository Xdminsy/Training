#!/usr/bin/python3
def getTimes(times):
    if times < 0:
        raise AttributeError('The attribute `times` cannot be less then 0')
    elif times == 1:
        return 'once'
    elif times == 2:
        return 'twice'
    else:
        return '%i times' % times
while True:
    line = input('>>> ')
    for i in 'aeiou':
        print("%c :" % i, getTimes(line.count(i)))
