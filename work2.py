#开放时间：2022/4/24 8:28

def Bmi(a,b):
    bmi=a/(b**2)
    if bmi<18.5:
        print('你的体重过轻')
    elif bmi<25:
        print('你的体重正常')
    elif bmi<28:
        print("你的体重过重")
    elif bmi<32:
        print('你的体重肥胖')
    else:
        print('你的体重严重肥胖')

if __name__ == '__main__':
    height = float(input('请输入你的身高'))
    weight = float(input('请输入你的体重'))
    Bmi(weight,height)