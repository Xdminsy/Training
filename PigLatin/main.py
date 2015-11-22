#!/usr/bin/python3
while True:
    line = input('>>>')
    while line[0] not in 'aeiou':
        line = line[1:] + line[0]
    line += "ay"
    print(line)
