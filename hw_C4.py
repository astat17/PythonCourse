a, b, c = int(input('')), int(input('')), int(input(''))
d = (b*b - 4*a*c)
if d > 0 or d == 0:
          x1 = (-b - d**0.5)/2/a
          x2 = (-b + d**0.5)/2/a
          print(x1, x2)
else:
          print('Корней нет')
