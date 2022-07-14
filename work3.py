#开放时间：2022/4/24 8:41
def Sum(*a):
    b=0
    for i in a:
         b+=i
    return b
print(Sum(1,23,4,5))

def Func2(a):
    lst=[]
    for i in a:
        if i%2==1:
            lst.append(i)
    return lst
lst=[1,2,3,4,5,6,7]
print(Func2(lst))

def Fun3(d):
    dict={}
    for key,value in d.items() :
        if len(value)>2:

            dict[key]=value[:2]
        else:
            dict[key]=value
    return dict
d={'name':'zs','horry':'sing'}
print(Fun3(d))
