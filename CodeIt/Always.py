# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.

# 거듭제곱은 '**' 으로 표현한다

# ord(),chr() 아스키코드?

# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)
a = int(input())
print('%x'%a)

# 올림 ceil
# 내림 floor
# 반올림 round

# 43    [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
# round로 해 주었더라도, 포멧을 항상 맞춰주는 것이 좋다.
a,b = map(float, input().split())
print(format(round(a/b,3),".3f"))

# 53 : [기초-논리연산] 참 거짓 바꾸기(설명)
a=bool(int(input()))
print(not a)

# 59 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)
# 파이썬은 and, not, or로 연산을하고 &,|,~은 비트 단위 연산자이다.
# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

# 63 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값

# 아직도 while문을 사용하는 데에 어려움이 있는 듯

# for문
# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)
# 형태로 수열을 표현할 수 있다. 시작 수는 포함이고, 끝 수는 포함되지 않는다. [시작, 끝)
# 증감할 수를 작성하지 않으면 +1이 된다.

# 78번 while true로 풀어보기

# 81 : [기초-종합] 16진수 구구단 출력하기
n = int(input(),16)
for i in range(1,int('f',16)+1):
    print("B*%X=%X" %(i,n*i))

#for와 while에서 continue의 역할에 대한 고찰이 필요할 듯!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
a = int(input())
b = 1
while a>=b:
    if(b%3 == 0):
        continue
    print(b, end=' ')
    b += 1
    # 이 코드는 틀렸음!!!!!!!!!!!!!!!!!