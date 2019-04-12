from math import log
a, b, N = int(input('a = ')), int(input('b = ')), int(input('N = '))
h, s = (b-a)/N, 0
for i in range(N):
          s += h/(log(a+i*h))
print(s)

#интеграл функции 1/ln(x) 
          
