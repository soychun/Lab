# https://www.acmicpc.net/problem/2750

import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
print(data)
print(sorted(data))
print(sorted(data,reverse=True))
data.sort()
print(data)