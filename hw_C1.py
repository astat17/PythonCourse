numbers = []
print('Введите числa. По окончании введите любой другой символ (не число)')
while True:
          try:
                    numbers.append(int(input('')))
          except ValueError:
                    break
def maximum (l:list = numbers):
          if len(l) == 1:
                    print (l[0])
          for i in range(1, len(l)):
                    if l[i-1]<l[i]:
                              print(l[i], end = ' ')
          print()
maximum()
# если ввод идет одной строкой (ч\з пробел)
a = [int(k) for k in input().split()]
maximum(a)

                    
          
