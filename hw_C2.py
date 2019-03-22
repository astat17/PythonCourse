#first version
n, multiplication, summa = input(''), 1, 0
for i in range((len(n))):
          multiplication *= int(n[i])
          summa += int(n[i])
print(multiplication, summa, sep = '  ')
#second version
n, multiplication, summa = int(input('')), 1, 0
while n != 0:
          multiplication *= n%10
          summa += n%10
          n = n//10
print(multiplication, summa, sep = '  ')
          
          


