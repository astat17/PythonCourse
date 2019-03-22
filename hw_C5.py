n, k = int(input('')), int(input(''))
do = 0
posle = 1
for i in range(1, n):
          do, posle = posle, do*k + posle
print(posle)
