import random
randint = random.randint(1,100)
count = 0
while(True):
    guess = int(input("请输入一个所猜测的数字（1-100）："))
    count += 1
    if(guess > randint):
        print("很遗憾，猜大了")
    if(guess < randint):
        print("很遗憾，猜小了")
    if(guess == randint):
        print("正确！")
        break
print("本轮竞猜次数为"+str(count))   

#添加一段注释     