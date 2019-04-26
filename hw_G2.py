def prime(n:int):
          a = True  
          for i in range(2, n):
                    if n%i == 0:
                              a = False
          if a:
                    return True
          else:
                    return False
def generator(n = 2):
          while True:
                    if prime(n):
                              yield n
                    n+=1
for n in generator():
          if n > 100:
              break
          print(n)


