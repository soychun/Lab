'''AAABB
AABAB

n=10,
K=24
두번째 B 위치 P를 구하시오
2진수로 나타냄'''


# 91 : [기초-종합] 함께 문제 푸는 날(설명)
# 3명이 다시 모여서 문제를 풀게 되는 날은 언제인가? 동시 가입/등업 후 며칠 후?
# input : 3,7,9
# output 63
# 수의 특징을 찾아서 문제를 풀어보자  / 일단 내가 가장 먼저 생각난 것은 최소 공배수 / 인수분해뱃
# 무식하게 구하기
a,b = map(int,input().split())


for i in range(max(a,b),a*b+1)