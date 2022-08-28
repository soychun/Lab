# 업로드 아직 안함

h,w = map(int,input().split())
n = int(input())
s = [[0 for _ in range(w+1)] for _ in range(h+1)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(n):
    # print('ll')
    l,d,x,y = map(int,input().split())
    if d==0:
        for i in range(l):
            # print(x,y+dy[2]*i)
            s[x][y+dy[2]*i] = 1
    elif d==1:
        for i in range(l):
            # print(x+dx[0]*i,y)
            s[x+dx[0]*i][y] = 1

for i in range(1,h+1):
    for j in range(1,w+1):
        print(s[i][j],end = ' ')
    print()