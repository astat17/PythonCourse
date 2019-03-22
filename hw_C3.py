n = input().split()
for i in range(len(n)):
          n[i] = len(n[i])
print(min(n))
#учитываем знаки препинания (в том числе и "?!", "!!!")
n = input().split()
for i in range(len(n)):
          if n[i].isalpha():
                    n[i] = len(n[i])
          else:
                    for k in n[i]:
                              if not k.isalpha():
                                        n[i] = n[i].replace(k, '')
                    n[i] = len(n[i])
                              
print(min(n))
