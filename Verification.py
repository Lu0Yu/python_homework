import random

code = []
for i in range(6):
    num = random.randint(33,126)
    word = chr(num)
    code.append(word)

for n in code:
    print(n,end='')
    
    
