# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.


# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)
a = int(input())
print('%x'%a)

# 43    [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
# round로 해 주었더라도, 포멧을 항상 맞춰주는 것이 좋다.
a,b = map(float, input().split())
print(format(round(a/b,3),".3f"))