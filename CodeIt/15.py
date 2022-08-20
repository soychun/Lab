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
'''int의 기능 중에서는, 진수를 표시하는 기능도 있다는 것을 잊지 말자!'''
a = int(input(),16)
print("%o"%a)

# 30
n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.

'''ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.  
실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다. A:65, B:66, C:67 .... 
ord(c) : 문자 c 를 10진수로 변환한 값 

컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화 되어야 하는데,
컴퓨터에 문자를 저장하는 방법으로 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다.

예를 들어, 영문 대문자 'A'는 10진수 값 65 로 표현하고, 
2진수(binary digit) 값 1000001 로 바꾸어 컴퓨터 내부에 저장한다. 

유니코드(unicode)는 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드이다.'''
a = ord(input())
print(a)

# 31
# chr( )는 정수값->문자, ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.
c = int(input())
print(chr(c))

# 32
a = int(input())
print(-a)

# 33
a = ord(input())
print(chr(a+1))

# 34
a,b = map(int,input().split())
print(a-b)

# 35
a,b = map(float,input().split())
print(a*b)

# 36
w,n = input().split()
print(w*int(n))
# for _ in range(int(n)):
#     print(w)
# 37
n = int(input())
s = input()
print(s*n)
# 38
a,n = map(int,input().split())
print(a**n)
# 39
# 거듭제곱은 '**' 으로 표현한다
a,n = map(float,input().split())
print(a**n)
# 40
# 몫은 '//' 으로 표현한다
a,b = map(int,input().split())
print(a//b)
# 41
# 나머지는 '%' 으로 표현한다
# python 언어에서는 나눈 나머지를 계산하는 연산자(%, remainder)를 제공한다.
# a%b 와 같이 작성하면, a를 b로 나눈 나머지(remainder)를 계산해준다.
# 나머지 연산(modulus, mod 연산)은 수학자 가우스가 생각해 낸 연산으로,
a,b = map(int,input().split())
print(a%b)

# 42
a = float(input())
print(format(a,".2f"))

# 43    [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
a,b = map(float, input().split())
print(format(round(a/b,3),".3f"))


