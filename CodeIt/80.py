'''AAABB
AABAB

n=10,
K=24
두번째 B 위치 P를 구하시오
2진수로 나타냄'''

# 95 : [기초-리스트] 바둑판에 흰 돌 놓기(설명
n=int(input())
l=[[0]*4]*4


for i in range(n):
    x,y =map(int,input().split())
    print(x,y)
    d[x][y]=1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(l[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()
print(l[0][1])
#
# print(len(l),len(l[0]))
