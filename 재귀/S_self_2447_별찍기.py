import sys
n = int(sys.stdin.readline())
first = ['***','* *','***']
#이것도 다시 풀어볼 것
def star(n,x):
    out = []
    if n==3:
        return x
    else:
        for i in x:
            out.append(i*3)
        for i in x:
            out.append(i+' '*len(x)+i)
        for i in x:
            out.append(i*3)
        return star(n//3,out)

final = star(n,first)
for i in final:
    print(i)


'''a = []
for i in first:
    print(i*3)
    a.append(i*3)
for i in first:
    print(i+'   '+i)
    a.append(i+'   '+i)
for i in first:
    print(i*3)
    a.append(i * 3)
for i in a:
    print(i)
second =a

for i in second:
    print(i*3)
for i in second:
    print(i+'   '*3+i)
for i in second:
    print(i*3)'''