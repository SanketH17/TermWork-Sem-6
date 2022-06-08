"""
Created on Sun Apr 3 23:02:50 2022
@author: COMPUTER
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 05:58:14 2022
@author: COMPUTER
Enter no. of non-terminals: 3
Enter no. of terminals: 3
Enter non-terminals
S
A
B
Enter terminals
c
b
a
Enter productions for:
S & c :

S & b :

S & a :
aABb
S & $ :

A & c :
c
A & b :

A & a :
aAc
A & $ :

B & c :
c
B & b :
bB
B & a :
"""

import re

r = int(input("Enter no. of non-terminals: "))
c = int(input("Enter no. of terminals: ")) + 1
non = []
ter = []
table = []
stack = ['$', 'S']
ptr = 0

print("Enter non-terminals")
for i in range(r):
    non.append(input())
print('Enter terminals')
for i in range(c - 1):
    ter.append(input())
ter.append('$')
print('Enter productions for: ')
temp_list = []

for i in range(r):
    for j in range(c):
        print(non[i], '&', ter[j], ':')
        temp_list.append(input())
    table.append(temp_list)

inp_str = input('Enter string to parse:') + '$'

while True:
    if re.match('[A-z]', stack[-1]) and inp_str[ptr] != '$':
        row = non.index(stack.pop())
        col = ter.index(inp_str[ptr])

        if table[row][col] != '*':
            temp = table[row][col][::-1]
        while temp != '':
            stack.append(temp[0])
            temp = temp.replace(temp[0], '')
        if stack[-1] == inp_str[ptr] and inp_str[ptr] != '$':
            ptr = ptr + 1
            stack.pop()
        if stack[-1] == '$':
            if inp_str[ptr] == '$':
                print('String is accepted')
                break
        else:
            print('String is not accepted')
            break
    elif inp_str[ptr] == '$':
        print('String is not accepted')
        break







