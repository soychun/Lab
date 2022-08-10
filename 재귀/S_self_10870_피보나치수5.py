# https://www.acmicpc.net/problem/10870

import sys
n = int(sys.stdin.readline())

def p(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return p(n-1)+p(n-2)

print(p(n))