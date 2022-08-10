# https://www.acmicpc.net/problem/10872
# 첫번째 쓴 코드
import sys
input = int(sys.stdin.readline())
def self_f(input):

    if input == 0:
        result = 1
    else:
        result = input * self_f(input - 1)

    return result

print(self_f(input))


# 수정한 코드
import sys
n = int(sys.stdin.readline())
def p(n):
    if n == 0:
        return 1
    else:
        return n*p(n-1)
print(p(n))

# 재귀에 대하여
# https://velog.io/@jewon119/01.%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B8%B0%EC%B4%88-%EC%9E%AC%EA%B7%80-%ED%98%B8%EC%B6%9CRecursive-Call%A0%EB%A6%AC%EC%A6%98-%EA%B8%B0%EC%B4%88-%EC%9E%AC%EA%B7%80-%ED%98%B8%EC%B6%9CRecursive-Call