#开放时间：2022/4/24 8:59
sum1=0
sum2=0
sum3=0
for i in range(1,11):
    sum1+=i
for i in range(20,31):
    sum2+=i
for i in range(35,46):
    sum3+=i
print(sum1,sum2,sum3)


#大和尚是a，小和尚是100-a

for i in range(0,34):
    if 3*i+(100-i)/3==100:
        break
print(i,100-i)

lst=[1,2,3,4,5,1,2,3,4]
s=set(lst)
print(s)

