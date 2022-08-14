# 한개의 정수를 입력 받을 때
import sys
n = int(sys.stdin.readline())

# 정해진 개수의 정수를 입력 받을 때
import sys
a,b = map(int,sys.stdin.readline().split())

# 임의의 개수의 정수를 입력 받을 때
import sys
n = list(map(int,sys.stdin.readline().split()))
print(n)
# input : 1 2 3 4 5
# output : [1, 2, 3, 4, 5]

# N줄의 숫자를 입력 받아 리스트에 저장할 때
import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
print(data)