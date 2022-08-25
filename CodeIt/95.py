# 95 : [기초-리스트] 바둑판에 흰 돌 놓기(설명
n=int(input())
l = [[0 for _ in range(20)] for _ in range(20)]

for i in range(n):
    x,y =map(int,input().split())
    l[x][y]=1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(l[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()
#
# print(len(l),len(l[0]))
