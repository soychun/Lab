import sys
n = int(sys.stdin.readline())
#다시 풀어볼 것. 여러가지 시도 하지 맣고 원론만 보는 것이 재귀를 푸는 방법인 듯 하다.

# 장대는 3개, 이동 횟추는 최소,
# def second():
# def third():
def hanoi(n,s,e,t):
    if n == 1:
        print(s,' ',e)
    else:
        hanoi(n-1,s,t,e)
        print(s,' ',e)
        hanoi(n-1,t,e,s)

hanoi(n,1,3,2)