i=123
f=3.14
s='Hello'

print('%i %f %s'%(i,f,s))
# 123 3.140000 Hello

print('i: %d, f: %f,s: %s'%(i,f,s))
# i: 123, f: 3.140000,s: Hello

print('i: %9d, f: %5.2f, s: %7s'%(i,f,s))
# i:       123, f:  3.14, s:   Hello

print('i: %09d, f: %05.2f, s: %7s' %(i,f,s))
# i: 000000123, f: 03.14, s:   Hello
# %5.2f에서 전체 5중에 '.'도 한칸을 차지한다고 간주한다



# .format() 이랑 f-string도 확인해 볼 것
# https://withcoding.com/64
# https://jimmy-ai.tistory.com/177
