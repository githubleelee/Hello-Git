import random
count = 0
##为了计轮数，加入count
c = 7
d = 11
e = 2
f = 3
g = 12 
##首先定义一些字母，这样再在后面重新定义这些字母就可以达到改变胜利与失败条件的目的
while True :
    a = random.randint(1,6)
    print('你掷出了%d点'%(a))
    b = random.randint(1,6)
    print('你掷出了%d点'%(b))
    count += 1
    print('第%d轮结束'%(count))
    num = a + b
    if num == c or num == d:
        print('恭喜你，您在第%d轮赢得了这场游戏！'%(count))
        break
    if num == e or num == f or num == g :
        print('很遗憾，您在第%d轮输掉了这场游戏。'%(count))
        break
    else :
        c = num 
        d = num
        e = 7
        f = 7
        g = 7
        ##第二轮开始，重新定义字母改变条件
    