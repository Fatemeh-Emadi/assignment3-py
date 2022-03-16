import random

arr=[]
a=1
b=50
flag=0
n=int(input("n="))
while len(arr)<n:
    temp=random.randint(a,b)
    if(temp in arr):
        flag=1
    else:
        arr.append(temp)

print(arr)


        
