s = []
for i in range(19):
    # print(i)
    s.append(list(map(int,input().split())))
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    a=a-1
    b = b-1
    for i in range(19):
        if(s[a][i]==1):
            s[a][i]=0
        elif(s[a][i]==0):
            s[a][i]=1
        for j in range(19):
            if(s[j][b] == 1):
                s[j][b] = 0
            elif(s[j][b] == 0):
                s[j][b] = 1
for i in range(19):
    for j in range(19):
        print(s[i][j],end =' ')
    print()
