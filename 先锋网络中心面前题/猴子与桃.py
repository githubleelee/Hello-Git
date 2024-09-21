while True :
    n = int(input("这是第几号猴子："))
    if n > 0 :
        break
    if n <= 0 :
        True
while True :
    m = int(input("还剩多少个桃："))
    if m > 0 :
        break
    if m <= 0 :
        True
##首先收集猴子的信息
m = int(m)
numb = m
## 不太会用for循环，这里尝试一下while循环
while n > 1 :
    numb = (numb * 2) + 1
    n -= 1
print('一开始共有%d个桃。'%(numb))