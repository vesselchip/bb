#开放时间：2022/4/24 8:03
#猜年龄小游戏，三次机会
#默认34岁


times=0
age=34
while times<=3:
    a=int(input('请输入猜测的年龄'))
    times += 1
    if a==age:
        print('恭喜你，你猜对了')
        break
    elif a>age:
        print('你猜大了，')
    else:
        print('你猜小了，')
    print(times)
    if times==3:
        choose=input('是否想要重新开始游戏y/n')
        if choose=='y':
            times=0
