#!/usr/bin/python3
import re, sys
text = sys.stdin.read()
match = re.findall(r'\b\w+?\b', text)
if match:
    print('There\'s %i words' % len(match))