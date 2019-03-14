import random
comp = random.randint(1,100)
while True:
          n = int(input(''))
          if n == comp:
                    print('Правильно')
                    break
          elif n > comp:
                    print('Ваше число больше, чем число компьютера')
          elif n < comp:
                    print('Ваше число меньше, чем число компьютера')
                    
