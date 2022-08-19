# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a)
# print(b)

'''참고
python의 input()은 한 줄 단위로 입력을 받는다.
input().split() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다.
a, b = 1, 2
를 실행하면, a에는 1 b에는 2가 저장된다.
(주의 : 하지만, 다른 일반적인 프로그래밍언어에서는 이러한 방법을 지원하지 않기 때문에 a=1, b=2 를 한 번에 하나씩 따로 실행시켜야 한다.)
'''

a,b = map(int, input().split())
print(a)
print(b)

# print 안에 컴마를 붙이면 한 칸 띄여져서 출력이 된다.
a,b = input().split()
print(b,a)

# print(c2, c1)
# 와 같은 방법으로 출력하면, c1과 c2에 저장된 값이 공백을 두고 순서가 바뀌어 한 줄로 출력된다.
# print( ) 안에서 쉼표(,)를 찍어 순서대로 나열하면, 그 순서대로 공백을 두고 출력된다.

a = input()
print(a,a,a)

# 18
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
# sep 는 분류기호(seperator)를 의미한다.

a,b = input().split(':')
print(a+':'+b)

# 19
a,b,c = input().split('.')
print(c,b,a,sep='-')

# 20
a,b = input().split('-')
print(a+b)

# 21
l = input()
for i in range(5):
    print(l[i])
# 22
s = input()
print(s[0:2],s[2:4],s[4:])

# 23
a,b,c = input().split(':')
print(b)
# 24
a,b = input().split(' ')
print(a+b)

# 25
# 입력되는 문자는 기본적으로 문자열로 인식된다.
a,b = map(int,input().split())
print(a+b)

# 26
a = float(input())
b = float(input())
print(a+b)

# 27  16진수는 x, 8진수는 o  ****************************
# 참고
# 10진수 형태로 입력받고
# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)

a = int(input())
print('%x'%a)

# 28   대문자!!
a = int(input())
print('%X'%a)

# 29
a = int(input(),16)
print("%o"%a)
